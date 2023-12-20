from adafruit_hid.keyboard import Keycode
"""
Macropad Hotkey: BLANK Horizontal
Description:

"""
app = {
  'name' : '[name here]', # Name of the macro
  'bmp' : '/path/to/bmp', # Path to .bmp image to display
  'animate' : False,
  'macros' : [ # List of button macros...
    # COLOR    LABEL    KEY SEQUENCE   PRESSED COLOR  SHORT LABEL
    (0x000000, '', [], 0x000000, ''), # 1st row ---------------
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''), # 2nd row ---------------
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''), # 3rd row ---------------
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, ''),
    (0x000000, '', [], 0x000000, '')  # encoder button
  ]
}