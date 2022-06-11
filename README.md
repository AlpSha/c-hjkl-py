# c-hjkl-py
Maps the Ctrl + h, j, k, l keys to Left, Down, Up, Right keys.
Also maps CapsLock to ESC key.
Written for dvorak layout. Support for other layouts can be added simply by changing the keycodes in src/keyboard_handler.py

# Why did you make this?
I've been using this repository. https://github.com/stewartpark/c-hjkl.git
But after re-installing my Arch Linux, it stopped working for my laptop's built-in keyboard.
As I'm not so familiar with Rust, I've decided to implement it using Python. Logic is pretty similar.

# How does it work?
It first detects the keyboards that are exist on the system. Then starts to absorbe their events. Creates a virtual device using Uinput module.
After mapping the keys, it passes the events to Uinput device. So your system gets the keyboard events through that virtual device.

# Can I change the Ctrl key to semothing else?
You can, simply by changing the keycode assigned to KEY_LEFTCTRL variable on src/keyboard_handler.py
