#!/usr/bin/env bash

install /opt/c-hjkl-py/c-hjkl /usr/local/bin
install /opt/c-hjkl-py/systemd/c-hjkl-py.service /etc/systemd/system
systemctl daemon-reload
systemctl enable --now c-hjkl-py.service
