# 4. Filming

Each task folder has a `FILM-DAY.md` with this checklist and the task's own commands.

## Before you press record

1. `odin-task build <task id>`: makes Goal.pdf, Metadata.rtf and the phone script, and flags
   mismatches (apps, placeholders, "Excel" in the narration).
2. `odin-mode on <task id>`: recording setup, plus the task's Goal at `/Users/Shared/Goal.pdf`
   and any input files in Downloads.
3. Browser (your tasking profile), **two separate windows**:
   - the work app (e.g. sheets.google.com), **minimized**,
   - `file:///Users/Shared/Goal.pdf`, on screen.
4. Cleanups: close Accessibility Inspector's window (keep it running), hide built-in AI
   buttons (Chrome's "Ask Gemini"), close side panels you won't use (the Sheets Tables panel).
5. **TaskRecorder:** paste the Goal (`pbcopy < <workspace>/tasks/<id>/goal.txt`) and list
   exactly the apps from the idea's Apps field.
6. **Studio fields:** Resolution, Light/Dark Mode (Dark), Dock position (Left), and "UI element
   changed" (Yes: wallpaper and dark mode). Then close Studio.
7. `odin-mode quit-apps`, Do Not Disturb on (Mac **and** phone), a quiet room, the phone script
   open on your phone.
8. Quit Claude. Command + Tab should show only Finder, the browser, TaskRecorder, Accessibility
   Inspector (and Insightful, minimized).

## While recording

- Click **Start Recording**, then TaskRecorder's yellow button to minimize it. Don't open it
  again until you stop.
- Intro under 20 s from the Goal window, minimize it, then go to the work window.
- One continuous take, **15:00–50:59**. No window may cover another.
- Follow the script. If a CHECK is wrong: say "Command Z", undo, and redo the row.
- Running late is fine; never skip a step to catch up. Never stop the epilogue early.
- Never on screen: AI tools, PII, Studio/Mercor/Slack, Metadata.rtf, Insightful's window.
- At the end: click TaskRecorder in the Dock, **Stop Recording**, then export the zip.

## Right after

- `odin-task package <task id>` (or ask Claude: "get this ready for submission"):
  - copies the files you downloaded during the recording into `deliverables/`
    (they become `final output 1`, `final output 2`, ... in download order),
  - makes `submit/` with the four upload files,
  - checks the video length and that TaskRecorder's Goal and apps match the idea,
  - prints the Studio steps.

  Input files you started from go in `inputs/` (they become `input 1`, ...). To choose the
  deliverables yourself, put them in `deliverables/` first (they're used in name order).
- Watch the video once: the intro, any CHECK you weren't sure of, the downloads, the last
  minutes (PII), and that the epilogue is 3+ minutes.
- `odin-mode off` when you're done for the day.

## A bad take

You can re-record. Delete the bad export from TaskRecorder's recordings folder (or move it
to the Trash) so `odin-task package` doesn't pick it up; it takes the newest zip unless you
pass one: `odin-task package <id> path/to/recording_123.zip`.
