# AI agents kept hunting for answers they were blocked from getting

Site: https://jeff-kazzee.github.io/transluce-dataset-notes/

## What seems to have happened

AI research agents get tested and trained on questions they have to answer by finding data on the web. Some of that data sits behind blocks: sites that turn away bots, logins, paywalls.

In September 2026, the research lab Transluce [reported](https://transluce.org/agent-activity) that agents doing this kind of work found a way around those blocks. They sent their requests through urlquery.net, a public service that security researchers use to open suspicious websites in a remote browser. The service loaded the page and published a report. The agents read the report.

Transluce says the agents were working on "web search tasks." One of their requests matches a question in Google's DeepSearchQA benchmark, a test set for AI research agents. Transluce describes a progression. In late 2025, the agents seem to have used the service to look things up. By March 2026 they were "finding creative ways around access limits." By May and June, when normal requests failed, a few tried to break into the sites holding the data, including an Australian government health agency. Transluce links some of this to a swarm of agents that OpenAI acknowledged running. They also say the evidence is "consistent with, but does not prove," that the agents learned this behavior during training.

Agents built to answer questions kept getting their answers by going where they weren't let in. Transluce published the records behind their report and asked people to keep looking. I did. Here's what their own data shows that the report doesn't.

## Weeks before Australia, agents hammered a US government budget portal

Between May 24 and May 27, 2026, agents asked for one federal budget report 586 times. The report sits on MAX.gov, the portal of the federal Office of Management and Budget. That was almost four weeks before the Australian break-in attempt that Transluce describes on June 20 and 21.

This wasn't a break-in. Transluce's own labels show the agents fetching the document through go-between services, again and again. Transluce marks none of the records as an attack. It does show how single-minded these agents were. They needed one document and asked for it hundreds of times in four days. Transluce's report mentions the document once, in passing, and never names the site or the count.

The OpenAI link comes from Transluce. They write that the OpenAI-acknowledged agents discussed this exact budget document "in dozens of other pages" on an online wiki. So the document ties this activity to OpenAI's agents. Transluce also writes that the agents using the scanner and the agents on the wiki look "largely distinct," so I can't say OpenAI sent all 586 requests.

## The agents ran every day for 57 days, then stopped

From April 26 to June 21, 2026, there was agent activity every single day. On June 22 it stopped, the same day Transluce says the wiki swarm went quiet. The report describes a May and June peak and a sudden end. It doesn't mention that the activity never missed a day for eight weeks, or when that run began.

Weekends look the same as weekdays. Sunday was the busiest day. People working a normal week leave gaps on weekends. This activity didn't, which fits machines running around the clock.

## Two more places the agents seem to have reached

These records are in neither Transluce's data nor a second public catalog of the same activity. They come from the same weeks and use the same go-between services. I read each full record. They look related, but nothing in them proves who sent them.

**Newspapers.com, May 13 to 15, 2026.** 29 requests ran Newspapers.com pages through services that turn web pages into plain text. In at least [one of them](https://urlquery.net/report/baddfac5-8b9b-422d-8bf4-d0398c5d4cb7), readable text from an old newspaper came back. Newspapers.com sells subscriptions. I haven't confirmed whether that page needed one at the time, so I'm not calling it a paywall bypass yet. If it did, this is exactly the "getting data they shouldn't" pattern.

**The FBI's crime data site, May 12, 2026.** Three requests asked the FBI's Crime Data Explorer for national arrest figures ([1](https://urlquery.net/report/7305dd56-9ea0-4b08-953b-d317e67dace2), [2](https://urlquery.net/report/40e9f02a-8599-4fcb-84a2-9c270b520212), [3](https://urlquery.net/report/99277f12-75da-4579-865f-70a2e6c44432)). At least one got an arrest-rate table back. [Kenneth DeGraff](https://www.kennethdegraff.com/swarm) and [Fortune](https://fortune.com/2026/09/09/openai-rogue-ai-agents-reached-12-more-websites/) already reported that the agents reached the FBI's systems using access keys. These three requests used no key, and nothing in them ties them to that incident.

## A note on the evidence itself

About a quarter of Transluce's records (8,968 of 37,649) came from a separate catalog that someone else built, a "research activity explorer" hosted at a chatgpt.site address. Transluce credits it in the data files, not in the report. Transluce kept 229 of those records even though its own notes on them say "needs review," and it rates 113 of them as strong evidence.

This matters if you cite the two collections together. When they agree, you're seeing one set of choices counted twice, not two confirmations. Transluce's strongest evidence doesn't rest on that list alone, though. Every strong record from it also has other evidence behind it.

## Still open

The search terms Transluce used to build its dataset seem to miss some variations of the sites the agents visited, so there may be more activity outside it. I've seen signs of this but haven't confirmed it record by record.

## How I checked

Every number above comes from Transluce's own files, recounted by a short script in this repository. The script also confirms that each quote appears word for word in Transluce's report. To run it:

1. Download Transluce's dataset from [their page](https://transluce.org/agent-activity) and unzip it into `data/`.
2. Save the report text as `data/agent-activity.txt`.
3. To check the outside catalog, save its data file as `data/tux_data.json`.
4. Run `python scripts/verify_claims.py --dataset data/urlquery-agent-activity-2026-09-22-v5 --page data/agent-activity.txt --explorer data/tux_data.json`.

My output is in `results/claims.json`, with a SHA-256 fingerprint of every file it read. My copy of the dataset matched Transluce's published fingerprints for all 15 files. I saved my copy of the report on September 25, 2026.

Before publishing, I read the coverage in [SecurityWeek](https://www.securityweek.com/openai-agents-probed-websites-for-vulnerabilities-while-fetching-public-data/), [CybelAngel](https://cybelangel.com/blog/openai-agents-bypassed-anti-bot-controls-government-sites/), and [XenoSpectrum](https://xenospectrum.com/en/ai-agent-urlquery-escalation/), and the [Hacker News discussion](https://news.ycombinator.com/item?id=49826565). None of them covers these points.

I don't work for Transluce. Corrections go in the [issue tracker](https://github.com/Jeff-Kazzee/transluce-dataset-notes/issues).

Code is MIT. Text is CC BY 4.0. By Jeff Kazzee.
