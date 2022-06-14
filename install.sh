#!/usr/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";

install "$SCRIPT_DIR/c-hjkl" /usr/local/bin
install "$SCRIPT_DIR/systemd/c-hjkl-py.service" /etc/systemd/system
systemctl daemon-reload
systemctl enable --now c-hjkl-py.service
