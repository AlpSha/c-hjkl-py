import evdev

class KeyboardHandler:
    def __init__(self, device: evdev.InputDevice):
        self.device = device

    def run_forever(self):
        for event in self.device.read_loop():
            print(evdev.categorize(event))


def new(device_path: str):
    return KeyboardHandler(evdev.InputDevice(device_path))

    
