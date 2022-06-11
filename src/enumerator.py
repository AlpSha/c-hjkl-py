from io import TextIOWrapper


class Keyboard:
    def __init__(self, name, path):
        self.name = name
        self.path = path

def enumerate_keyboards():
    try:
        file = open('/proc/bus/input/devices', 'r')
    except:
        print('Unable to open /proc/bus/input/devices')
        return []
    entries = collect_device_entries(file)
    keyboards = []
    for entry in entries:
        if entry['handler'] == None:
            continue
        if entry['ev'] != '120013':
            continue
        path = '/dev/input/' + entry['handler']
        keyboards.append(Keyboard(entry['name'], path))
    return keyboards


def collect_device_entries(file: TextIOWrapper):
        entries = []
        entry = {}
        for line in file:
            if line == '\n':
                entries.append(entry)
                entry = {}
                continue
            parts = line.split('=')
            value = parts[1].replace('"', '').strip()
            if line.startswith('N: Name='):
                entry['name'] = value
            elif line.startswith('H: Handlers='):
                allHandlers = value.split(' ')
                entry['handler'] = next(handler for handler in allHandlers if handler.startswith('event'))
            elif line.startswith('B: EV='):
                entry['ev'] = value
            else:
                continue
        return entries
    
