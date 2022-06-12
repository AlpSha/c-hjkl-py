import sys
import time
import evdev
from evdev import UInput
from evdev.ecodes import EV_KEY
import enumerator

KEY_ESC = 1;
KEY_LEFTCTRL = 29;
KEY_CAPSLOCK = 58;
KEY_H = 36;
KEY_J = 46;
KEY_K = 47;
KEY_L = 25;
KEY_UP = 103;
KEY_LEFT = 105;
KEY_RIGHT = 106;
KEY_DOWN = 108;

class KeyboardHandler:
    def __init__(self, device: evdev.InputDevice, uinput: UInput):
        self.device = device
        self.uinput = uinput

    def run_forever(self):
        try:
            time.sleep(1)
            ctrl_pressed = False
            self.device.grab()
            for event in self.device.read_loop():
                if event.type != EV_KEY:
                    self.uinput.write_event(event)
                    self.uinput.syn()
                    continue
                if event.code == KEY_LEFTCTRL:
                    ctrl_pressed = event.value != 0
                if event.code == KEY_CAPSLOCK:
                    event.code = KEY_ESC
                if event.value >= 1 and ctrl_pressed:
                    key_to_press = 0
                    if event.code == KEY_H:
                       key_to_press = KEY_LEFT
                    elif event.code == KEY_K:
                        key_to_press = KEY_UP
                    elif event.code == KEY_L:
                        key_to_press = KEY_RIGHT
                    elif event.code == KEY_J:
                        key_to_press = KEY_DOWN

                    if key_to_press > 0:
                        self.uinput.write(EV_KEY, KEY_LEFTCTRL, 0)
                        self.uinput.write(EV_KEY, key_to_press, 1)
                        self.uinput.write(EV_KEY, key_to_press, 0)
                        self.uinput.write(EV_KEY, KEY_LEFTCTRL, 0)
                        self.uinput.syn()
                        continue
                
                self.uinput.write_event(event)
                self.uinput.syn()
        except:
            print("Problems....")
            print(sys.exc_info()[0])



def new(keyboard: enumerator.Keyboard):
    return KeyboardHandler(evdev.InputDevice(keyboard.path), UInput(name=keyboard.name))


