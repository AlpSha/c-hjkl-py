import time

from enumerator import enumerate_keyboards

def run_forever_until_keyboards_change():
    count = None
    while True:
        keyboards = enumerate_keyboards()
        if count == None:
            count = len(keyboards)
        if count != len(keyboards):
            break
        time.sleep(1)

