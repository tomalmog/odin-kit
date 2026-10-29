# 3. Recording scripts

A script turns the approved idea into timed rows you read from your phone while recording.
`templates/SCRIPT.md` is the skeleton and `examples/painting-quote/SCRIPT.md` is a complete
one. `odin-task build` turns SCRIPT.md into `Script (phone).pdf`, one card per row.

## Format

- Sections follow the idea's Steps, in order: `## 1. Create the sheet (0:20–1:20)`.
- Each row is `| time | Do | Say |`:
  - **Time** is the real clock time you should reach that row.
  - **Do** is one or two actions, naming the exact element (`A1`, **Bold**, **File > Download**).
  - **Say** is the narration, in quotes.
- A row whose Do contains **✅ CHECK** becomes an orange card: the exact value or look to
  verify before moving on (e.g. "D10 is **760**", "the cells **show a $ sign**").
- A line starting with **⏱** becomes a purple pace card ("about 13:20 on the clock here").
- Required sections: `## Intro`, `## After you stop` and `## Numbers to expect` (a table
  of every expected value, so you can check yourself).

## Rules (all from real reviews and AutoQC findings)

**Intro (under 20 seconds)**
- The Goal is open in its **own browser window** (not a tab next to the work).
- The first line is exactly: *"I will be beginning my task soon. Here is the workflow I have
  in mind."*
- Then one sentence on who you are and what you're making, minimize the Goal window, and
  switch to the work window. Don't read the whole task out (no more than 30 s on it).

**Narration**
- Say **what** you're doing, **where** it is on screen (the exact element), and **why** for any
  decision that isn't obvious. A listener with closed eyes should be able to follow.
- Say every keyboard shortcut out loud ("I'm copying with Command C").
- Pause about a second after each click. Never go silent for more than 45 seconds; keep
  talking while you type.
- Call apps by their names. **Never say "Excel"** for Google Sheets; for the download, say "the
  .xlsx option".

**Building**
- **One or two actions per row.** Long rows get skipped or done wrong on camera.
- **Copy formulas with Command + C / Command + V**, not the fill handle (dragging goes wrong
  easily). Use absolute references (`$B$2`) when a copied formula must keep pointing at one cell.
- **Practise the formulas before recording**, so no minutes go on fixing them.
- **Add a ✅ CHECK after every tricky step**, with the exact expected number.

**Formatting**
- Format every result: money as currency, rates as %, counts as plain numbers (watch for
  Sheets carrying $ onto a count; fix it with Format > Number > Number).
- Make the % click **its own row**, with a CHECK that literally reads "the cells show a % sign".
  It's the most often skipped step.
- Conditional formatting: set **both** the text colour and the fill colour explicitly.
- Summary values must say what they are about. For example, "Best month" shows *which* month,
  not just the amount.
- Charts select only the rows their title promises, with a CHECK on the number of bars.

**Files**
- **Download every deliverable on camera**, then show them in Finder > Downloads in list view
  (Command + 2).
- **Never press Space or double-click a file in Finder.** Quick Look counts as using the
  Preview app, which then has to be in the Apps list.

**Epilogue (required: 3–4 minutes, after the Finder step)**
- Go back to the work and cover: **the result** (with the key number), **how you checked it**
  (a formula in the formula bar plus one sum by hand), **challenges**, **limitations**, and
  **what you'd improve**. A plain recap isn't enough.
- Writers consistently run short here. Give the epilogue 10–11 talking points about 25 s
  apart, and a hard rule: **don't stop before <time>**, at least 4 minutes after the Finder step.

## Pacing: write real clock times

Everyone underestimates. Time each row at about **60 seconds of real clock time** for a row
of one or two actions with narration, then calibrate after your first take:

1. Note the clock time you actually reached the Finder step, and how many task rows you had.
2. Divide: seconds per row = (Finder time − 20 s) / rows.
3. Use that for every later script.

Then check the totals: the video must be between **15:00 and 50:59**. Aim for 20–25 minutes.

## Writing a script with Claude

Give Claude the approved idea text and ask for SCRIPT.md in this repo's format (CLAUDE.md
tells it the rules). Check the "Numbers to expect" table by working the numbers out yourself,
then rehearse the formulas once in a scratch sheet before filming.
