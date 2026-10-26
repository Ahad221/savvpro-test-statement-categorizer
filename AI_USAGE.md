# AI Usage

## Tools used

- Claude (claude.ai chat): [fill in the model/plan you used]. Used for
  planning, writing code phase by phase, and explaining it.
- [Any other tool: Copilot, ChatGPT, etc. Delete this line if none.]

## What AI did and what I did

AI helped plan the phases, draft code for each phase and write tests. I made
these decisions myself: [fill in, e.g. chose the landlord use case, chose the
mortgage split as the signature feature, set the review threshold, chose the
categories]. I ran every phase locally, read the files before committing, and
used small commits per phase.

## Where the AI was wrong or I had to fix things

1. **Duplicate row pointed at itself.** Row 60 said "Possible duplicate of row
   60". I noticed it when reading the API response. The cause was storing the
   CSV line number (header = line 1) while the output uses an index starting at
   1, so they were off by one. Fixed by storing the output index. [Add the
   test name you wrote for it.]
2. **Empty rules file.** [Describe it in your own words. It was an unsaved
   file on my side, not an AI mistake, and I should say so.]
3. **Tests count mismatch.** [If something like this happened: the AI's test
   count differed from mine and what I did.]
4. [Add 1-2 more real moments you remember. Reviewers value specific, honest
   examples more than a long list.]

## How I verified the AI's output

- Ran `pytest` after every phase.
- Called the API manually in Swagger and checked totals by hand: the mortgage
  interest and principal total of -$14,389.20 equals 12 x $1,199.10; the
  security deposit nets to $0.00.
- Tested the UI end to end on the sample statement.

## Token usage

[Claude chat does not show per-message token counts. Add a screenshot of any
usage page your account provides, and say honestly that exact counts are not
available if that is the case. Do not estimate numbers as if they were real.]

Screenshots are in `docs/ai-usage/`.# AI Usage

## Tools used

- Claude (claude.ai chat): [fill in the model/plan you used]. Used for
  planning, writing code phase by phase, and explaining it.
- [Any other tool: Copilot, ChatGPT, etc. Delete this line if none.]

## What AI did and what I did

AI helped plan the phases, draft code for each phase and write tests. I made
these decisions myself: [fill in, e.g. chose the landlord use case, chose the
mortgage split as the signature feature, set the review threshold, chose the
categories]. I ran every phase locally, read the files before committing, and
used small commits per phase.

## Where the AI was wrong or I had to fix things

1. **Duplicate row pointed at itself.** Row 60 said "Possible duplicate of row
   60". I noticed it when reading the API response. The cause was storing the
   CSV line number (header = line 1) while the output uses an index starting at
   1, so they were off by one. Fixed by storing the output index. [Add the
   test name you wrote for it.]
2. **Empty rules file.** [Describe it in your own words. It was an unsaved
   file on my side, not an AI mistake, and I should say so.]
3. **Tests count mismatch.** [If something like this happened: the AI's test
   count differed from mine and what I did.]
4. [Add 1-2 more real moments you remember. Reviewers value specific, honest
   examples more than a long list.]

## How I verified the AI's output

- Ran `pytest` after every phase.
- Called the API manually in Swagger and checked totals by hand: the mortgage
  interest and principal total of -$14,389.20 equals 12 x $1,199.10; the
  security deposit nets to $0.00.
- Tested the UI end to end on the sample statement.

## Token usage

[Claude chat does not show per-message token counts. Add a screenshot of any
usage page your account provides, and say honestly that exact counts are not
available if that is the case. Do not estimate numbers as if they were real.]

Screenshots are in `docs/ai-usage/`.