from playsound import playsound
import os
import time

CODES = {
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
    'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', ' ': '/', '!': '-·-·--', '.': '·-·-·-', ',': '--··--'
}

INTERVAL = 0.3  # sec


def sleep(mult):
    time.sleep(INTERVAL * mult)


def play_sound(sound='dot'):
    path = os.path.join(os.path.dirname(__file__), f'{sound}.mp3')
    playsound(path)


text = input('enter text (unsupported characters will be ignored): ').strip().lower()

for i, char in enumerate(text):
    if char not in CODES:
        continue
    elif char == ' ':
        print(' ', end='')
        if text[i - 1] == '.':
            print(' ' * 5, end='')
            sleep(5)
        else:
            print(' ' * 3, end='')
            sleep(3)
    else:
        code = CODES.get(char)
        for symbol in code:
            if symbol == '.':
                print('.', end='')
                play_sound('dot')
            else:
                print('-', end='')
                play_sound('dash')
    print(' ', end='')
    sleep(1)
