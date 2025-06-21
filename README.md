# c-hjkl-py

Lightweight Python tool to remap `Ctrl + H/J/K/L` to arrow keys and `CapsLock` to `ESC` — optimized for Dvorak users.

---

## ✨ What It Does

- Maps `Ctrl + H` to ←, `Ctrl + J` to ↓, `Ctrl + K` to ↑, `Ctrl + L` to →
- Remaps `CapsLock` to `ESC`
- Works by intercepting input events and forwarding them through a virtual keyboard
- Designed for Dvorak layout, but easily adaptable

---

## 🤔 Why This Exists

I was using [stewartpark/c-hjkl](https://github.com/stewartpark/c-hjkl), but after reinstalling Arch Linux, it stopped working for my laptop’s built-in keyboard.

Since I’m not super familiar with Rust and wanted to debug it quickly, I reimplemented the core logic in Python.

---

## ⚙️ How It Works

1. Detects connected keyboards on your system.
2. Listens to their input events using `evdev`.
3. Creates a virtual device using the `uinput` module.
4. Translates your key combos and emits remapped events.

Your system receives input from the virtual keyboard instead of the physical one.

---

## 🔧 Can I Customize Keys?

Yes.

To change the key used for triggering remaps (e.g., `Ctrl` to something else), edit:

```python
# In src/keyboard_handler.py
KEY_LEFTCTRL = 29  # Change this to your desired key
```

You can also modify other mappings by tweaking the keycode logic in the same file.

---

## 🛡️ Security Notice

> ⚠️ **IMPORTANT:** Run and install this tool as the `root` user only.
>
> Since it runs with elevated privileges and hooks low-level input devices, make sure that:
>
> * Your normal user cannot modify the project files.
> * You clone it into a protected directory (e.g., `/opt/`).

This prevents privilege escalation in case your user account gets compromised.

---

## 🚀 Installation

```bash
sudo su
cd /opt
git clone https://github.com/AlpSha/c-hjkl-py.git
cd c-hjkl-py
./install.sh
```

---

## 🧱 Dependencies

* Python 3
* `evdev` Python package
* `uinput` kernel module (make sure it’s loaded)

Install `evdev` via pip if needed:

```bash
pip install evdev
```

---

## 🧪 Tested On

* Arch Linux (x86\_64)
* Dvorak layout

---

## 🧩 TODO / Future Plans

* Layout support toggle
* GUI tray icon
* Hotkey customization via config file

---

## 📜 License

MIT

---

Made with caffeine and key rage by Alp.
