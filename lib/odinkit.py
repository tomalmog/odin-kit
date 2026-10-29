"""Shared settings for the odin-kit tools.

Settings live in ~/.odin-kit/config.json (made by install.sh from config.example.json).
Any key missing from that file falls back to DEFAULTS, so an older config keeps working.
Set ODIN_KIT_HOME to use a different settings folder (handy for testing).
"""
import json
import os
import subprocess
import tempfile
from pathlib import Path

HOME = Path.home()
KIT_HOME = Path(os.environ.get("ODIN_KIT_HOME", HOME / ".odin-kit")).expanduser()
CONFIG_FILE = KIT_HOME / "config.json"
STATE_DIR = KIT_HOME / "state"
KIT_ROOT = Path(__file__).resolve().parent.parent

DEFAULTS = {
    # Where task folders live: <workspace>/tasks/<task id>/
    "workspace": "~/odin",
    # The only apps pinned to the Dock while recording. Running apps still show up on their own.
    "dock_apps": ["/Applications/Google Chrome.app", "/Applications/TaskRecorder.app"],
    # Odin needs the Dock on the left or right, never the bottom.
    "dock_side": "left",
    # Apps to reopen when you leave Odin mode (quit-apps closes everything else before filming).
    "reopen_on_off": [],
    # Bundle ids that `odin-mode quit-apps` leaves running: the recording apps, Insightful,
    # Claude (quit it by hand last) and the terminals that run these tools.
    "keep_running": [
        "com.google.Chrome",
        "com.apple.finder",
        "com.google.anvil.TaskRecorder2",
        "com.apple.AccessibilityInspector",
        "com.workpuls.Agent",
        "com.anthropic.claudefordesktop",
        "com.apple.Terminal",
        "com.googlecode.iterm2",
    ],
    # AI apps whose background helpers outlive the app. TaskRecorder logs every process, so
    # quit-apps stops these outright.
    "ai_app_bundles": [
        "/Applications/ChatGPT.app",
        "/Applications/Codex.app",
        "/Applications/Cursor.app",
        "/Applications/Kimi.app",
        "/Applications/Antigravity.app",
        "/Applications/OpenCode.app",
    ],
    # Built-in solid colours, used in turn so each recording looks different from the macOS
    # default (AutoQC's UI-diversity check compares against the default look).
    "wallpapers": [
        "/System/Library/Desktop Pictures/Solid Colors/Plum.png",
        "/System/Library/Desktop Pictures/Solid Colors/Red Orange.png",
        "/System/Library/Desktop Pictures/Solid Colors/Ocher.png",
        "/System/Library/Desktop Pictures/Solid Colors/Dusty Rose.png",
        "/System/Library/Desktop Pictures/Solid Colors/Gold.png",
        "/System/Library/Desktop Pictures/Solid Colors/Space Gray.png",
    ],
    # Dark mode counts as a UI change; light mode is the macOS default and doesn't.
    "dark_mode": True,
    # Move the Desktop and Downloads out of view while recording (put back by `off`).
    "hide_desktop_and_downloads": True,
}


def load():
    config = dict(DEFAULTS)
    if CONFIG_FILE.exists():
        config.update(json.loads(CONFIG_FILE.read_text()))
    return config


def workspace(config):
    return Path(config["workspace"]).expanduser()


def tasks_dir(config):
    return workspace(config) / "tasks"


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def print_pdf(page, pdf):
    """Print an HTML file to PDF with headless Chrome (no header or footer)."""
    if not Path(CHROME).exists():
        raise SystemExit("Google Chrome is needed to make PDFs. Install it, then try again.")
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", f"--user-data-dir={profile}",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf}", Path(page).resolve().as_uri()],
                       capture_output=True, check=True)
