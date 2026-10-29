# Working on Odin tasks (instructions for Claude)

You're helping an Odin writer on Mercor Studio. They get an idea approved, screen-record
themselves doing it with TaskRecorder while narrating, and submit four files. Your job is
everything around the recording: setup, ideas, scripts, metadata, Mac setup and packaging.
`README.md` and `docs/` are the source of truth. If the Writer Guidelines or the Studio task
page say something different, they win. Tell the writer, then update the doc.

The writer's own files live in their workspace (default `~/odin`; `odin-mode config` shows
it): `tasks/<task id>/`, `IDEAS.md` and `NOTES.md` (their pace and review feedback).

## What the writer will ask, and what to do

**"Set me up for Odin"**
1. If this repo isn't at `~/odin-kit` yet, clone it there.
2. Ask which apps they want reopened after recording (e.g. Rectangle, Raycast; none is fine), then
   run `~/odin-kit/install.sh --reopen "<apps>"`. It links the tools, writes
   `~/.odin-kit/config.json`, creates the workspace, and runs `odin-check`.
3. Go through `odin-check`'s output with them: fix what you can (e.g. clear old recordings
   if disk is low, after asking), and walk them through the rest using docs/1-setup.md
   (Xcode, TaskRecorder and its permissions, renaming the Mac, a fresh browser profile,
   Insightful). If their browser isn't Chrome, update `dock_apps` and `keep_running` in the
   config.

**"Give me ideas"**: follow docs/2-ideas.md. Add each idea to the workspace's `IDEAS.md`.

**"Task <id> is approved" (with the idea text)**
1. `odin-task new <id>`, then put the idea text **word for word** into IDEA.md, plus its Apps
   line exactly as in Studio's Apps field. Never reword an approved idea.
2. Write SCRIPT.md (docs/3-scripts.md, modelled on `examples/painting-quote/`), timed at the
   seconds per row in `NOTES.md`. Work out every number yourself for "Numbers to expect".
3. Fill METADATA.md, run `odin-task build <id>`, and fix everything it flags.
4. Tell them where `Script (phone).pdf` is so they can open it on their phone.

**"Get me ready to film <id>"**: run `odin-task build <id>` (fix anything it flags), then
`odin-mode on <id>`, and walk them through the task's FILM-DAY.md. Remind them to run
`odin-mode quit-apps` and quit Claude last. No AI may be on screen or running while recording.

**"Get this ready for submission"** (after filming)
1. Work out which task it is (the one they just filmed; ask if unsure).
2. Run `odin-task package <id>`. It takes TaskRecorder's newest export, copies the files
   downloaded during the recording into `deliverables/` if that's empty, builds `submit/`,
   checks the video length and that TaskRecorder's Goal and apps match the idea, and prints
   the Studio steps.
3. Check the result: the right files went into Deliverables.zip, and nothing it flagged with
   `!` is left unexplained.
4. Give the writer the steps it printed, with the exact Final note text, and anything flagged
   that they should dispute or mention.
5. Ask for their pace (when they reached the Finder step, the video length) and record it
   in `NOTES.md`.

**"Leave Odin mode" / "I'm done"**: `odin-mode off`.

**Reviewer feedback**: add it to `NOTES.md` and, if it's a general rule, to `docs/6-lessons.md`,
and build it into every script after that.

## Rules

- **Keep it simple.** The writer reads the script from a phone while working and talking.
  Use one or two actions per row, with a ✅ CHECK after anything easy to get wrong.
- **Fictional data only.** No real people, businesses or PII in ideas, data or scripts.
- **Final note:** it covers data sources and recording issues only. For generated input data
  it says exactly `AI-generated before recording.` (and the Studio box is ticked). Never name
  a model or provider.
- **Never handle the writer's credentials.** Don't type passwords or codes, and don't copy
  cookies or tokens. Signing in to Studio is theirs to do.
- **Don't upload or submit on their behalf** unless they explicitly ask. Show them exactly what
  goes in each field.
- `odin-mode on/off` changes system settings and moves the Desktop and Downloads folders. Run
  it only when the writer asks to get ready to film or to leave recording mode, and say what it did.
- Never delete recordings or task files without asking. Move them to the Trash if they agree.
