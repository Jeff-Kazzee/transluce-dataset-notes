# What's in Transluce's agent dataset that the article doesn't say

On September 23, 2026, Transluce published [its report on AI agents that used urlquery.net](https://transluce.org/agent-activity) to get around blocks and sometimes probe websites. They released the data and asked people to keep digging, so I did. Everything below comes from their own files. One script, `scripts/verify_claims.py`, recomputes every number and checks every quote. Run it instead of trusting me.

Site: https://jeff-kazzee.github.io/transluce-dataset-notes/

## Agents requested a federal budget report 586 times in four days

From May 24 to May 27, 2026, Transluce's dataset has 586 urlquery reports tagged `MAX budget documents`. MAX.gov is the portal of the Office of Management and Budget (OMB). The article mentions this task once, as a single wiki link to "a scan of a federal budget data PDF." It doesn't name MAX.gov or give the count.

Transluce tags 267 of these reports as source requests, 318 as relay use, and 1 as a custom program. None of their notes on these reports mention a probe or an exploit. The agents asked for the same document over and over.

The OpenAI link comes from Transluce's write-up. They say this PDF "is discussed by wiki agents in dozens of other pages," and they describe that wiki traffic as something "which OpenAI has publicly acknowledged as originating from them." Their `methods.json` calls the PDF the "Exact document linked from wiki to a URLQuery report."

So the shared document ties this task to the OpenAI swarm. Transluce also writes that the urlquery agents and the wiki agents look "largely distinct," so I can't say OpenAI sent all 586 requests.

## A quarter of the dataset comes from an outside catalog

8,968 of the 37,649 included reports carry the note "Member of the externally selected research-activity cohort." Transluce's `methods.json` names the source of that cohort, a "research activity explorer" at `research-activity-september-2026.tuxianeer.chatgpt.site`, dated September 21, 2026. All 8,968 reviewed urlquery rows in that explorer are in Transluce's dataset.

The article doesn't mention the explorer. The credit appears only in the data files.

Transluce includes 229 of those rows even though their own note starts "Explicit reference or discovery candidate; relation to an agent-like workflow needs review." It rates 113 of the 229 as significant.

Every significant row that cites the outside cohort also lists other evidence, so the significant set doesn't rest on the explorer alone. The two catalogs still aren't independent. If you see them agree, you're looking at one selection counted twice.

## The activity ran 57 days without a gap

Every UTC day from April 26 through June 21, 2026, has at least 10 included reports. June 22 has none. The article describes a May and June peak that collapses on June 22. It doesn't say that the run never skipped a day or that it started on April 26.

Weekends show no drop. Since March 1, Sunday has the most active days (19) and Tuesday the fewest (12).

## Open questions

Some reports on the same tasks seem to fall outside the dataset because the search patterns miss domain variants. For example, the pattern `*whssgr.com*` in `methods.json` doesn't match `whssgrgupkar.com`. My counts for these come from urlquery search results, and I haven't checked them record by record. I'm listing them as questions, not findings.

## Check the numbers

1. Download Transluce's dataset from their page and unzip it into `data/`.
2. Save the article text as `data/agent-activity.txt`. My copy from September 25, 2026, has SHA-256 `b82ec342e6d313384c44bbf1abac993114638684579aedeb4e57472869a57908`.
3. For the explorer cross-check, save its data JSON as `data/tux_data.json`.
4. Run the script:

   ```
   python scripts/verify_claims.py --dataset data/urlquery-agent-activity-2026-09-22-v5 --page data/agent-activity.txt --explorer data/tux_data.json
   ```

`results/claims.json` holds my output and the SHA-256 hash of every input.

## Limits

"Not in the article" means I couldn't find it in my saved copy of the page. The page can change. On September 25, 2026, I searched news coverage, Hacker News, and the web and found no one else writing about these points. That doesn't prove no one has. I'm not affiliated with Transluce. If I got something wrong, open an issue.

Code is MIT. Text is CC BY 4.0. By Jeff Kazzee.
