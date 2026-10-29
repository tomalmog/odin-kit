# odin-kit

A tested workflow for Mercor's **Odin** project. An idea gets approved, you screen-record
yourself doing the task with TaskRecorder while narrating, then you submit four files in Studio.

> Keep this repo private and share it only with Odin writers. Rules change, so the Writer
> Guidelines and the Studio task page always win over anything here.

## Setup: one command

Open Claude Code and say:

> Set me up for Odin with the odin-kit repo at `<repo URL>`.

Claude clones it to `~/odin-kit`, asks which of your apps to reopen after recording, and
runs the installer. Or do it yourself:

```bash
git clone <repo URL> ~/odin-kit && ~/odin-kit/install.sh
```

The installer:
- puts `odin-mode`, `odin-task` and `odin-check` on your PATH,
- writes your settings to `~/.odin-kit/config.json`,
- creates your workspace (`~/odin`, with `tasks/`, `IDEAS.md`, `NOTES.md` and a `CLAUDE.md`),
- checks your Mac against Odin's requirements.

Then finish the one-time setup in **[docs/1-setup.md](docs/1-setup.md)**: Xcode, TaskRecorder and
its permissions, renaming the Mac, a fresh browser profile and Insightful.

## Every task, as you'd say it to Claude

| You say | What happens |
|---|---|
| "Give me some simple Google Sheets ideas." | Ideas in Odin's five-heading format, logged in `IDEAS.md` |
| "Task abc123 is approved: <idea text>." | `tasks/abc123/` with the idea, a timed script, metadata, the Goal page and a phone PDF of the script |
| "Get me ready to film abc123." | Odin mode on (Dock, clock, dark mode, a new wallpaper, a clean Desktop and Downloads, Accessibility Inspector), plus the film-day checklist |
| *(you film, then export from TaskRecorder)* | |
| "Get this ready for submission and tell me the steps." | `submit/` with the four upload files, checked against the idea, plus the exact Studio steps and Final note |
| "I'm done, leave Odin mode." | Your Mac back to normal, and your usual apps reopened |

The same steps as commands:

| Step | Command |
|---|---|
| Check the Mac | `odin-check` |
| Make a task folder | `odin-task new <task id>` |
| Make the Goal page, Metadata.rtf and phone script, and check they agree | `odin-task build <task id>` |
| Recording setup (with the task's Goal and inputs) | `odin-mode on <task id>` |
| Quit everything a recording doesn't need | `odin-mode quit-apps` |
| Package for submission and print the Studio steps | `odin-task package <task id>` |
| Back to normal | `odin-mode off` |
| Where things stand | `odin-mode status`, `odin-task list`, `odin-mode config` |

## The docs

1. [Setup](docs/1-setup.md): one time, plus what Odin mode changes and its settings
2. [Ideas](docs/2-ideas.md): the idea box, what gets approved, the apps rule
3. [Scripts](docs/3-scripts.md): the script format, the review rules and pacing
4. [Filming](docs/4-filming.md): before, during and after the recording
5. [Submitting](docs/5-submitting.md): the four files, AutoQC, disputes and the final checks
6. [Lessons](docs/6-lessons.md): what real reviews and AutoQC flagged, and the fix for each

`examples/painting-quote/` is a complete, ready-to-film task (idea, script, metadata).

## Layout

```
install.sh    one-command setup
bin/          odin-mode, odin-task, odin-check, make-phone-script
lib/          shared code (settings, PDF printing, phone-script layout)
templates/    files for new task folders and the workspace
examples/     painting-quote, a complete example task
docs/         the workflow, step by step
CLAUDE.md     how Claude Code should help (it reads this automatically in this folder)
```

## Settings

`~/.odin-kit/config.json`: which apps to reopen after recording, the Dock apps (use your
recording browser), the Dock side, the apps `quit-apps` leaves running, and the workspace
folder. See [docs/1-setup.md](docs/1-setup.md#settings-odin-kitconfigjson).

## Requirements

macOS 15+, Xcode (it provides `/usr/bin/python3` and Accessibility Inspector), Google Chrome
(used to make the PDFs), and TaskRecorder 2.4.4.
