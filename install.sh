#!/bin/bash
# One-command setup: link the tools, write the settings, create the workspace, check the Mac.
#
#   ./install.sh                         asks which apps to reopen after `odin-mode off`
#   ./install.sh --reopen "Rectangle, Raycast"   no questions (what Claude runs)
#   ./install.sh --workspace ~/work/odin         put task folders somewhere other than ~/odin
set -euo pipefail

KIT="$(cd "$(dirname "$0")" && pwd)"
BIN="$HOME/.local/bin"
CONFIG_DIR="${ODIN_KIT_HOME:-$HOME/.odin-kit}"
CONFIG="$CONFIG_DIR/config.json"
reopen=""
reopen_given=no
workspace="~/odin"

while [ $# -gt 0 ]; do
  case "$1" in
    --reopen) reopen="${2:-}"; reopen_given=yes; shift 2 ;;
    --workspace) workspace="${2:?--workspace needs a folder}"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; sed -n '2,6p' "$0" >&2; exit 1 ;;
  esac
done

mkdir -p "$BIN" "$CONFIG_DIR"
for tool in odin-mode odin-task odin-check make-phone-script; do
  chmod +x "$KIT/bin/$tool"
  ln -sf "$KIT/bin/$tool" "$BIN/$tool"
done
echo "Linked odin-mode, odin-task, odin-check and make-phone-script into $BIN"

if [ -f "$CONFIG" ] && [ "$reopen_given" = no ]; then
  echo "Kept your settings in $CONFIG"
else
  if [ "$reopen_given" = no ] && [ -t 0 ]; then
    echo
    echo "odin-mode quit-apps closes everything a recording doesn't need."
    read -r -p "Apps to reopen when you leave Odin mode (comma-separated, e.g. Rectangle, Raycast; Enter for none): " reopen || true
  fi
  REOPEN="$reopen" WORKSPACE="$workspace" /usr/bin/python3 - "$KIT/config.example.json" "$CONFIG" <<'PY'
import json, os, sys
source = sys.argv[2] if os.path.exists(sys.argv[2]) else sys.argv[1]
config = json.load(open(source))
config["reopen_on_off"] = [a.strip() for a in os.environ["REOPEN"].split(",") if a.strip()]
config["workspace"] = os.environ["WORKSPACE"]
json.dump(config, open(sys.argv[2], "w"), indent=2)
open(sys.argv[2], "a").write("\n")
PY
  echo "Wrote $CONFIG"
fi

ws="$(/usr/bin/python3 -c "import json,os,sys;print(os.path.expanduser(json.load(open(sys.argv[1]))['workspace']))" "$CONFIG")"
mkdir -p "$ws/tasks"
for file in CLAUDE.md IDEAS.md NOTES.md; do
  if [ ! -f "$ws/$file" ]; then
    sed "s|{kit}|$KIT|g" "$KIT/templates/workspace/$file" > "$ws/$file"
  fi
done
echo "Workspace ready: $ws (tasks/, IDEAS.md, NOTES.md, CLAUDE.md)"

case ":$PATH:" in
  *":$BIN:"*) ;;
  *) if ! grep -qs '.local/bin' "$HOME/.zshrc"; then
       echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
       echo "Added ~/.local/bin to your PATH in ~/.zshrc (open a new terminal to use the commands)"
     fi ;;
esac

echo
"$KIT/bin/odin-check" || true
