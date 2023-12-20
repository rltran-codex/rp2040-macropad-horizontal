7# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

# Note: when using this, the macropad needs to be rotated where the USB-C cable coming from the top

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'del', [Keycode.BACKSPACE]),
        (0x120149, '1', ['1']),
        (0x120149, '4', ['4']),
        (0x120149, '7', ['7']),
        # 2nd row ----------
        (0x120149, '0', ['0']),
        (0x120149, '2', ['2']),
        (0x120149, '5', ['5']),
        (0x120149, '8', ['8']),
        # 3rd row ----------
        (0x101010, '', []),
        (0x120149, '3', ['3']),
        (0x120149, '6', ['6']),
        (0x120149, '9', ['9']),
        # Encoder button -- -
        (0x000000, '', [Keycode.KEYPAD_ENTER])
    ]
}
