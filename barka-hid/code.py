import digitalio
import board
from time import sleep
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

button = digitalio.DigitalInOut(board.GP24)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

TEXT = '''Pan kiedys stanal nad brzegiem,
Szukal ludzi gotowych pojsc za Nim;
By lowic serca
Slow Bozych prawda.
Ref.: O Panie, to Ty na mnie spojrzales,
Twoje usta dzis wyrzekly me imie.
Swoja barke pozostawiam na brzegu,
Razem z Toba nowy zaczne dzis low.
2. Jestem ubogim czlowiekiem,
Moim skarbem sa rece gotowe
Do pracy z Toba
I czyste serce.
Ref.: O Panie, to Ty na mnie spojrzales,
Twoje usta dzis wyrzekly me imie.
Swoja barke pozostawiam na brzegu,
Razem z Toba nowy zaczne dzis low.
3. Ty, potrzebujesz mych dloni,
Mego serca mlodego zapalem
Mych kropli potu
I samotnosci.
Ref.: O Panie, to Ty na mnie spojrzales,
Twoje usta dzis wyrzekly me imie.
Swoja barke pozostawiam na brzegu,
Razem z Toba nowy zaczne dzis low.
4. Dzis wyplyniemy juz razem
lowic serca na morzach dusz ludzkich
Twej prawdy siecia
I slowem zycia.
Ref.: O Panie, to Ty na mnie spojrzales,
Twoje usta dzis wyrzekly me imie.
Swoja barke pozostawiam na brzegu,
Razem z Toba nowy zaczne dzis low'''

sleep(0.2)
while True:
    if not button.value:
        keyboard.send(Keycode.WINDOWS, Keycode.R)
        sleep(0.2)
        layout.write('notepad')
        sleep(0.2)
        keyboard.send(Keycode.ENTER)
        sleep(0.2)
        layout.write(TEXT, delay=0)
        sleep(0.2)