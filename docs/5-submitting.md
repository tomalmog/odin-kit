# 5. Submitting

## The four uploads

`odin-task package <task id>` puts them all in `tasks/<id>/submit/`, then prints these
steps with your file names and Final note filled in:

| Studio field | File |
|---|---|
| Screen recording | `video.mp4`, taken out of the TaskRecorder zip |
| TaskRecorder export | the unmodified `recording_<number>.zip` |
| Deliverables | `Deliverables.zip`: `input 1…`, `artifact 1…`, `final output 1…`, each with its original extension (a code project goes in a folder named `final output 1`) |
| Metadata | `Metadata.rtf`, in **its own field**, never inside Deliverables.zip |

Large files take a while. Keep the Mac awake while uploading (`caffeinate -dimsu` in a
terminal), keep the Studio tab in the foreground, and don't let the laptop sleep on battery.

**Careful:** if you upload the same file to two tasks, Studio may share it, and deleting it
from one task can empty the other. Double-check each field's file name after uploading.

## Metadata.rtf

Three fields (no Apps field):
- **Topology:** every app visit in order, repeating apps you return to, each tagged LOOKUP,
  CREATE or MODIFY. Example: `Google Sheets (CREATE) -> Finder (LOOKUP)`.
- **Request:** exactly the Goal pasted into TaskRecorder (odin-task fills it in from IDEA.md).
- **Task Description:** a numbered, high-level summary of the voice-over.

Delete the template's example section if you start from Studio's template instead.

## AutoQC

Studio runs automated checks after you upload: file and recording checks first (about 37), then
narration checks about 10 minutes later. Checks marked "blocks submit" must pass or be
disputed.

**Disputing a finding:** click **Dispute** under it, explain in "Explain why this finding is
wrong", then **Submit dispute**. It then shows "Disputed". Only dispute when you're right,
and explain briefly with facts (what's on screen, what a reviewer told you before).

Common findings:
- **UI diversity:** the recording must differ from the macOS default look (light mode, default
  wallpaper). Odin mode's dark mode plus solid-colour wallpaper covers it.
- **Used Apps:** every app in the idea's Apps field must be in TaskRecorder's Used Apps.

## Before Submit for Review

1. **The five setup questions** ("1. Install Xcode … 5. Set your clock and Dock: did you do this
   step?") must all be "Yes, I did this step". They're dropdowns that appear one at a time and
   can be blank again on each new task.
2. **The manual checks:** about 25 boxes (task plan, preparation, recording, video spot checks,
   narration, content). Tick each only after checking it against your recording. They include:
   typing at most 20% of the video, the task not narrated for more than 30 s at the start,
   Accessibility Inspector in the Dock with a dot, the Dock visible at the start and end, and no
   Studio/Mercor/Airtable on screen.
3. **The Final note:**
   - No input files: `No input files; all values typed during recording.`
   - Generated input data: tick **"AI-generated before recording"** in Studio and write exactly
     `AI-generated before recording.` Don't name the model or provider.
   - Downloaded input files: list the source URLs (free CC0 or public-domain files only).
   - Mention recording issues a reviewer should know about. Keep it factual and short.
4. Click **Submit for Review**. If nothing happens, wait for "Autosaving" to finish and click
   again; if Studio lists missing items, fix those.

After a successful submit, the page says "Submit for Review completed successfully" and the
status moves to Routing, then Quick Review or In Review.

## Reviews

A reviewer sends 1–2 sentences with timestamps and the exact element to fix. A task gets at
most 4 review rounds. Add every piece of feedback to `docs/6-lessons.md` (or your own notes)
so the next script builds it in.
