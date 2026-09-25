# Notes on Transluce's urlquery agent-activity dataset

On 2026-09-23, Transluce published [Early rogue AI agent activity and attempts to hack found on urlquery.net](https://transluce.org/agent-activity) and released the dataset behind it. They asked readers to keep digging. These are three things we found in their public files. Each number below comes from one script, `scripts/verify_claims.py`, which you can run yourself.

Site: https://jeff-kazzee.github.io/transluce-dataset-notes/

## 1. Agents chased a US federal budget report through urlquery 586 times in four days

Source: Transluce's public dataset of urlquery.net reports.

Between 2026-05-24 and 2026-05-27, the dataset holds 586 reports in its `MAX budget documents` bucket (584 suggestive, 2 significant), out of 597 in total. MAX.gov is the Office of Management and Budget (OMB) portal. Transluce labels these 586 as source requests (267), relay or intermediary use (318), and one custom program. None of their reason texts mentions a probe or exploit. As far as the labels show, this was retrieval, not a hack.

How it ties to OpenAI, in Transluce's own words:

- The article says the wiki "links directly to urlquery.net exactly once, on May 26, pointing to a scan of a federal budget data PDF" and that "this PDF is discussed by wiki agents in dozens of other pages."
- It describes the DseWiki traffic as something "which OpenAI has publicly acknowledged as originating from them."
- The dataset's `methods.json` identifies the document as a MAX PDF: "Exact document linked from wiki to a URLQuery report."

What this supports: the urlquery activity chased the same federal document that the OpenAI-acknowledged wiki agents were working on. What it does not prove: that every one of the 586 scans came from OpenAI. Transluce itself writes that "it seems like the individual agents involved were largely distinct" between urlquery and the wiki.

The article mentions the PDF once. It does not name MAX.gov or say how many reports the dataset holds for it.

## 2. Nearly a quarter of the included reports come from an outside catalog

8,968 of the 37,649 included reports (24%) carry the reason "Member of the externally selected research-activity cohort." The dataset's `methods.json` names the source: a "research activity explorer" at `research-activity-september-2026.tuxianeer.chatgpt.site`, dated 2026-09-21. All 8,968 reviewed urlquery rows in that explorer appear in the dataset.

- The article text does not mention the explorer or the cohort. The credit is in the data files.
- 229 of these included rows have reason text that begins "Explicit reference or discovery candidate; relation to an agent-like workflow needs review." 113 of them are rated significant.
- Every significant row that cites the cohort also lists other evidence. This does not show that the significant set rests on the explorer alone.

Why it matters: readers who treat the dataset and the explorer as two independent sources would be counting the same selection twice.

## 3. The activity ran 57 days without a break

From 2026-04-26 to 2026-06-21, every UTC day has at least 10 included reports. On 2026-06-22 there are none. Since March 1, Sunday has the most active days (19) and Tuesday the fewest (12). There is no weekend dip.

The article describes a May and June peak that collapses on June 22. The unbroken run and its start date are not in the text.

## Open questions, not findings

Some reports on the same tasks may sit outside the dataset because the search patterns miss domain variants. For example, the pattern `*whssgr.com*` in `methods.json` does not match `whssgrgupkar.com`. Other cases include percent-encoded URLs. Our counts for these come from urlquery search results and are not yet verified record by record, so we list them as questions only.

## Reproduce

1. Download Transluce's dataset package from their page and unzip it into `data/`.
2. Save the article text to `data/agent-activity.txt`. Our copy, fetched 2026-09-25, has SHA-256 `b82ec342e6d313384c44bbf1abac993114638684579aedeb4e57472869a57908`.
3. Optional: save the explorer's data JSON to `data/tux_data.json` for the cross-check in claim 2.
4. Run:

   ```
   python scripts/verify_claims.py --dataset data/urlquery-agent-activity-2026-09-22-v5 --page data/agent-activity.txt --explorer data/tux_data.json
   ```

`results/claims.json` holds our output, including SHA-256 hashes of every input file.

## Limits

- "Not in the article" means no match in our saved copy of the page text. The page may change.
- We searched news coverage, Hacker News, and the web on 2026-09-25 and found no prior write-up of these points. Absence of results does not prove nobody published them.
- We have no affiliation with Transluce. Corrections are welcome as issues.

Code: MIT. Text: CC BY 4.0.
