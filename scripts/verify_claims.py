"""Recompute every published claim from Transluce's public files. Writes results/claims.json.

Inputs (download them yourself, see README):
  --dataset   folder of Transluce's v5 package (all-reports.csv, report-sources.csv)
  --page      saved text of https://transluce.org/agent-activity
  --explorer  optional: the research activity explorer data JSON, for claim 2's cross-check

Usage:
  python scripts/verify_claims.py --dataset data/urlquery-agent-activity-2026-09-22-v5 \
      --page data/agent-activity.txt [--explorer data/tux_data.json]
"""

import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

COHORT = "externally selected research-activity cohort"
NEEDS_REVIEW = "Explicit reference or discovery candidate"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(dataset):
    csv.field_size_limit(10**9)
    reports = list(csv.DictReader(open(Path(dataset) / "all-reports.csv", encoding="utf-8")))
    sources = list(csv.DictReader(open(Path(dataset) / "report-sources.csv", encoding="utf-8")))
    return reports, sources


def claim_max(reports, sources, page_text):
    by_id = {r["report_id"]: r for r in reports}
    rows = [by_id[s["report_id"]] for s in sources if s["data_source"] == "MAX budget documents"]
    window = [r for r in rows if "2026-05-24" <= r["report_date_utc"][:10] <= "2026-05-27"]
    return {
        "source_bucket": "MAX budget documents",
        "reports": len(rows),
        "reports_2026_05_24_to_27": len(window),
        "confidence_in_window": dict(Counter(r["confidence"] for r in window)),
        "page_mentions_max_gov": page_text.lower().count("max.gov"),
    }


def claim_cohort(reports, explorer_path):
    cohort = [r for r in reports if COHORT in r["why_included"]]
    flagged = [r for r in cohort if r["disposition"] == "included" and r["why_included"].startswith(NEEDS_REVIEW)]
    significant = [r for r in reports if r["confidence"] == "significant"]
    out = {
        "rows_citing_external_cohort": len(cohort),
        "cohort_confidence": dict(Counter(r["confidence"] for r in cohort)),
        "included_cohort_rows_with_needs_review_reason": len(flagged),
        "needs_review_rows_by_confidence": dict(Counter(r["confidence"] for r in flagged)),
        "significant_rows_total": len(significant),
        "significant_rows_citing_cohort": sum(COHORT in r["why_included"] for r in significant),
        "example_needs_review_ids": sorted(r["report_id"] for r in flagged)[:5],
    }
    if explorer_path:
        data = json.load(open(explorer_path, encoding="utf-8"))
        ids = {r["report_id"].replace("-", "") for r in cohort}
        reviewed = [row for row in data["rows"] if data["classifications"][row[13]][0] == "reviewed_urlquery_cohort"]
        out["explorer_updated"] = data.get("updated")
        out["explorer_reviewed_urlquery_rows"] = len(reviewed)
        out["explorer_reviewed_rows_in_transluce_cohort"] = sum(row[0] in ids for row in reviewed)
    return out


def claim_run(reports):
    per_day = Counter(r["report_date_utc"][:10] for r in reports if r["disposition"] == "included")
    best, start, cur = (0, None, None), None, 0
    day, end = date(2025, 11, 1), date(2026, 9, 21)
    while day <= end:
        if per_day.get(day.isoformat(), 0) >= 10:
            start = start or day
            cur += 1
            if cur > best[0]:
                best = (cur, start, day)
        else:
            start, cur = None, 0
        day += timedelta(days=1)
    days = [datetime.strptime(d, "%Y-%m-%d") for d in per_day]
    weekday = Counter(d.strftime("%a") for d in days if d >= datetime(2026, 3, 1))
    return {
        "longest_run_days_with_10_plus_reports": best[0],
        "run_start": best[1].isoformat(),
        "run_end": best[2].isoformat(),
        "reports_on_day_after_run": per_day.get((best[2] + timedelta(days=1)).isoformat(), 0),
        "active_days_by_weekday_since_2026_03_01": dict(weekday),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--page", required=True)
    ap.add_argument("--explorer")
    a = ap.parse_args()
    reports, sources = load(a.dataset)
    page_text = Path(a.page).read_text(encoding="utf-8")
    result = {
        "inputs": {
            "all-reports.csv": sha256(Path(a.dataset) / "all-reports.csv"),
            "report-sources.csv": sha256(Path(a.dataset) / "report-sources.csv"),
            "page_text": sha256(a.page),
            **({"explorer": sha256(a.explorer)} if a.explorer else {}),
        },
        "max_budget_documents": claim_max(reports, sources, page_text),
        "external_cohort": claim_cohort(reports, a.explorer),
        "continuous_run": claim_run(reports),
    }
    out = Path(__file__).resolve().parent.parent / "results/claims.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
