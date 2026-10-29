# 2. Ideas

Every task starts with an idea that Studio has to approve. An automated Idea Check reads it,
and the recording is later checked against it, so the steps, the Apps list and the recording
must all match. Missing or inconsistent items are the most common reason ideas get sent back.

## The idea box

All five headings, each filled in:

```
Domain / Role: the field and who would do it.

Goal: one sentence: what you make, with the key calculations, and the deliverable.

Starting materials: from scratch, or the input files (describe them: rows, columns, source).

Steps (with the apps for each):
1. Google Sheets: ...
2. Google Sheets: ...
...
N. Finder: open the Downloads folder and confirm the files are there.

Deliverable: the final output(s), named, with what they contain.
```

Then the **Apps** field: type each app from the Steps and press Enter.

## What gets approved and films well

- **Something a professional really does**, explained with expertise: invoices, quotes,
  pay stubs, purchase orders, expense claims, budgets, simple comparisons.
- **Fits one continuous take of 15:00–50:59**, including a short intro and a 3–4 minute
  epilogue. Aim for about 20–25 minutes.
- **Mostly mouse work.** Typing may be at most about 20% of the video, so keep data entry to
  short tables (5–6 rows).
- **Narratable step by step:** every click is on a named element, with no silence over 45 s.
- **Simple:** one or two formula patterns (multiply, SUM, subtract), standard formatting
  (bold, font size, currency, %, a fill colour). Avoid multi-tab builds, lookups, pivot tables
  and anything that's easy to get wrong on camera.

## Rules that send ideas or recordings back

- **Apps:** list only the apps you actually work in. For Sheets work that's **Google Sheets**
  and **Finder** (for the final Downloads check). Don't list the browser (Chrome or Safari)
  as a separate app. Add **Preview** only if you open or Quick Look a file.
- **The idea's Apps field, TaskRecorder's Used Apps and the Metadata Topology must name the
  same apps.** AutoQC flags a Major if the idea lists an app that TaskRecorder doesn't.
  Watch Studio's Apps suggestions: picking "Chrome (G-Sheets)" or "Other - Google Chrome"
  adds Chrome.
- **No restricted apps** (check the list in Studio). TextEdit is banned except for making
  Metadata.rtf. Excel desktop has recording problems; use Google Sheets.
- **Input files:** free files only (CC0 or public domain), or data generated before recording
  and declared as such (see docs/5-submitting.md). No real people's data, no private PII.
  Starting from scratch with typed fictional values avoids the question entirely.
- **Every deliverable is downloaded on camera** (e.g. File > Download > PDF and .xlsx), and the
  idea's last step checks them in Finder.
- **No AI on screen while recording.** Plan everything before.

## Sizing an idea

At a first-timer's pace, one script row (one or two actions plus narration) takes about a
minute of real time. So:

| Rows of work | Task part | Plus intro and epilogue |
|---|---|---|
| 15 | ~15 min | ~20 min |
| 19 | ~19 min | ~24 min |

Under 15:00 total is rejected, so if in doubt, add a step (a check, a formatting pass, a
note line) rather than cut one.

## Example

See `examples/painting-quote/IDEA.md`: a quote built from scratch in Google Sheets, with a
header, five lines, a cost column, subtotal, tax and total, then a PDF and .xlsx download.
