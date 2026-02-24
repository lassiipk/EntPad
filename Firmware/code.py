print(
    
    "Smash as hard as possiable on the pad!. Just Kiddding just kidding...\
       Please dont smash hard, it might brake the pad, so be gentle with it... PLEASE!!!!\
       Made with ♥ by SAIM "

)

# Importing libraries

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Delay
from kmk.scanners import DiodeOrientation

# ------------ Keyboard Setup --------------
# Setting up the keyboard

keyboard = KMKKeyboard()

# ------------ Pin Assigning --------------
# Setting up the pins for the keyboard, and the diode orientation

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----------- Macro Setup ---------------
# Setting up the macros


# ------------ Keymap --------------
# keymap

keyboard.keymap = [

    [KC.NO, KC.NO, KC.NO,
     KC.NO, KC.ENT, KC.NO,
     KC.NO, KC.NO, KC.NO],

]

if __name__ == '__main__':
    keyboard.go()