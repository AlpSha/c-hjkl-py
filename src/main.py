import sys
import threading
import detector
import keyboard_handler


# HACK: Keyboard detection thread. If it detects change, program stops and systemd restarts it again
def listen_keyboards():
    detector.run_forever_until_keyboards_change()
    print('Keyboard(s) are added/removed. Exitting...')
    sys.exit(2)


def main():
    threading.Thread(target=listen_keyboards)
    keyboards = detector.enumerate_keyboards()

    threads = []
    for keyboard in keyboards:
        print('Found keyboard: ' + keyboard.name)
        handler = keyboard_handler.new(keyboard.path)
        t = threading.Thread(target=handler.run_forever)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()

