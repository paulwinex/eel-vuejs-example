import eel
import random


@eel.expose
def get_value():
    return random.randrange(10000, 9999999)


eel.init('web')

try:
    eel.start('main.html', size=(500, 200))
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
