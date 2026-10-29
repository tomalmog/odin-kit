# Film day: task {task}

## Before filming
1. **Run `odin-task build {task}`** and fix anything it flags.
2. **Run `odin-mode on {task}`.** It applies the recording setup and puts the Goal at
   `/Users/Shared/Goal.pdf`. If Odin mode is already on, it just loads this task.
3. **Browser (your work profile), two separate windows:**
   - **Window 1:** the app you start in (e.g. sheets.google.com), then **minimize it**.
   - **Window 2:** `file:///Users/Shared/Goal.pdf`, left on screen.
4. **Cleanups:**
   - close **Accessibility Inspector's** window (keep it running),
   - hide any built-in AI buttons (e.g. Chrome's "Ask Gemini"),
   - close side panels you won't use (e.g. the Sheets **Tables** panel).
5. **TaskRecorder:** run `pbcopy < {workspace}/tasks/{task}/goal.txt` and paste the Goal. List
   exactly the apps in the idea's Apps field (see IDEA.md).
6. **Studio:** fill in Resolution, Light/Dark (**Dark** with Odin mode), Dock position, and
   "UI element changed" = **Yes (wallpaper + dark mode)**. Then close the Studio tab.
7. **Run `odin-mode quit-apps`**, turn on **Do Not Disturb** on the Mac and phone, and open
   **Script (phone).pdf** on your phone.
8. **Quit Claude**, and check Command + Tab shows only Finder, the browser, TaskRecorder and
   Accessibility Inspector (plus Insightful if you track time).

## Film
- Start Recording, click TaskRecorder's **yellow button**, and say the intro (**under 20 s**).
- Minimize the Goal window, then click your work window in the Dock.
- Follow the script. Orange cards = number checks, purple = pace checks. **No Space or
  double-click in Finder** (that opens Quick Look, which counts as the Preview app).
- Click TaskRecorder in the Dock and click **Stop Recording**, then export the zip.

## After
1. Move the files you downloaded on camera into `tasks/{task}/deliverables/`.
2. Run `odin-task package {task}`. It makes `submit/` with the four upload files.
3. In Studio: upload the four files, run AutoQC, answer the setup questions, tick the
   checks, add the Final note, and click **Submit for Review** (see docs/5-submitting.md).
4. Run `odin-mode off` and turn off Do Not Disturb.
