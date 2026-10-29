# 6. Lessons from real tasks

Collected from reviews, AutoQC findings and takes that went wrong. Each one is already built
into the templates and docs; this is the why.

| What happened | The fix |
|---|---|
| A fill-handle drag copied a formula the wrong way and cost several minutes on camera | Copy with Command + C / V, and add a ✅ CHECK with the expected number after it |
| The take ran about 1.5x longer than the script's times, twice in a row | Write real clock times, about 60 s per row, and recalibrate after each take |
| The epilogue lasted about 2 minutes when it needed 3–4 | 10+ talking points and a hard "don't stop before" clock time |
| Percentages were left as decimals (0.3698) in the deliverable, twice | The % click gets its own row and a CHECK that the cells show a % sign |
| A chart included rows its title didn't promise | Select only the rows the chart is about, CHECK the bar count |
| Quick Look in Finder was logged as Preview, which wasn't in the Apps list | Never press Space or double-click in Finder, or list Preview |
| The .xlsx wasn't downloaded on camera | Download every deliverable on camera, then show them in Finder |
| Narration said "Excel" for Google Sheets | Say "Google Sheets", and "the .xlsx option" for the download |
| The intro didn't use the standard opening line | Open with "I will be beginning my task soon. Here is the workflow I have in mind." |
| The Goal was a tab next to the work, not its own window | Open Goal.pdf in a separate window and minimize it after the intro |
| Light mode was flagged as "no UI change" | Light is the macOS default; Odin mode uses dark mode and a solid-colour wallpaper |
| A calendar widget and "Ask Gemini" were visible | Odin mode hides widgets; hide in-app AI buttons by hand |
| An AI app's helper processes kept running in the background | `odin-mode quit-apps` stops them |
| The idea's Apps field listed Chrome, TaskRecorder didn't: AutoQC Major | The idea, TaskRecorder and Topology list the same apps; keep the browser out |
| Submit was blocked by blank setup questions | Answer all five "did you do this step?" dropdowns on each task |
| "Best month" showed only an amount | Summary values say which item they're about |
| Conditional formatting kept Sheets' default green fill | Set both the text colour and the fill |
| A small step (renaming a tab, a border) was forgotten | Keep ideas simple, and give every step in the idea its own script row |

Add your own as you get reviews.
