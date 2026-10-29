# 1. One-time setup

Do this once, before your first task. Studio won't let you submit until the five
setup questions on every task page are answered "Yes, I did this step", so do them properly.

## Mac requirements

- Apple silicon (M1 or newer), or Intel with macOS 15+ (Intel uses the Intel TaskRecorder installer).
- macOS 15 or newer.
- At least 35 GB free. A 30-minute recording is about 2–3 GB, and TaskRecorder keeps every
  export in `~/Library/Application Support/TaskRecorder/recordings/`.

## Studio's five setup steps

1. **Install Xcode** from the Mac App Store. Open it once so it finishes installing its
   components. Accessibility Inspector comes with it.
2. **Turn on Accessibility Inspector.** It has to be running during every recording, with its
   window closed. `odin-mode on` starts it for you.
3. **Install TaskRecorder 2.4.4** from the Download TaskRecorder card on the task page (there
   is also a Google Drive backup link for Apple silicon).
4. **Give TaskRecorder its permissions:** in System Settings > Privacy & Security, allow
   Screen Recording, Accessibility, Microphone and Input Monitoring. Then make a short test
   recording and check that the video and audio work.
5. **Clock and Dock:** the clock must show the date and seconds, and the Dock must be on
   the left or right (not the bottom). `odin-mode on` sets both.

## Privacy setup

PII means an automatic send-back. One frame or one spoken sentence with your full name,
photo, personal email or an account is enough.

- **Rename your Mac** (System Settings > General > About > Name), e.g. "MacBook Pro". The name
  shows up in Finder and in sharing dialogs.
- **Use a fresh browser profile** only for tasking: no history, saved addresses, bookmarks
  or personal avatar. On first launch, skip importing and don't sign in to a browser account.
  Sign in only to what the tasks need (e.g. a Google account for Sheets that doesn't show your
  real name).
- Keep **Mercor Studio, Slack and Insightful off screen** while recording.

## Insightful (time tracking)

Install Insightful and sign in with your @mercor.expert account. Run the Odin timer while
you work on hourly tasks and pause it for breaks. Insightful may stay running during a
recording, but its window must not be visible: minimize it (its icon may show in the Dock).

## Install odin-kit

```bash
git clone https://github.com/tomalmog/odin-kit ~/odin-kit && ~/odin-kit/install.sh
```

(Or ask Claude Code: "Set me up for Odin with the odin-kit repo at https://github.com/tomalmog/odin-kit.")

The installer:
- links `odin-mode`, `odin-task`, `odin-check` and `make-phone-script` into `~/.local/bin`, and
  adds that folder to your PATH in `~/.zshrc`,
- creates `~/.odin-kit/config.json`, asking which apps to reopen when you leave Odin mode
  (`--reopen "Rectangle, Raycast"` skips the question),
- creates your workspace, `~/odin` (or `--workspace <folder>`), with `tasks/`, `IDEAS.md`,
  `NOTES.md` and a `CLAUDE.md` pointing Claude at this kit,
- runs `odin-check`, which lists anything still missing from this page.

Run `odin-check` again any time. Running `install.sh` again is safe: it keeps your settings
and files.

### What `odin-mode on` changes (and `off` puts back)

| Setting | In Odin mode |
|---|---|
| Dock | left (or right), always visible, only your browser and TaskRecorder pinned |
| Clock | date and seconds shown |
| Appearance | dark mode (light is the macOS default and doesn't count as a UI change) |
| Wallpaper | a built-in solid colour, a different one for each recording |
| Desktop | moved to `~/Documents/Desktop items` |
| Downloads | moved to `~/Downloads-hold`, so the folder is empty on camera |
| Desktop widgets | hidden |
| Handoff | off, so apps open on your phone don't appear in the Dock |
| Accessibility Inspector | started |

Your normal settings are saved in `~/.odin-kit/state/` first, and `odin-mode off` restores
them, moves your files back, and reopens the apps listed in `reopen_on_off`.

`odin-mode quit-apps` quits every app a recording doesn't need (everything not in
`keep_running`) and stops background helpers of AI apps, because TaskRecorder logs every
running process. Quit Claude by hand last.

### Settings (`~/.odin-kit/config.json`)

| Key | What it does |
|---|---|
| `workspace` | where task folders live (`<workspace>/tasks/<task id>/`), default `~/odin` |
| `dock_apps` | apps pinned to the Dock while recording. Use your recording browser's path |
| `dock_side` | `left` or `right` |
| `reopen_on_off` | app names to reopen after `odin-mode off`, e.g. `["Rectangle", "Raycast"]` |
| `keep_running` | bundle ids `quit-apps` leaves alone. Add your browser's if it isn't Chrome (Safari is `com.apple.Safari`, Firefox is `org.mozilla.firefox`) |
| `ai_app_bundles` | AI apps whose helpers get stopped before recording |
| `wallpapers` | the solid colours to rotate through |
| `dark_mode` | switch to dark mode in Odin mode |
| `hide_desktop_and_downloads` | move the Desktop and Downloads out of view |

To find an app's bundle id: `osascript -e 'id of app "Firefox"'`.
