# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name': 'Firefox',  # Application name
    'bmp' : '/images/firefox_logo.bmp',
    'animate' : False,
    'macros': [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'Back One Page', [Keycode.ALT, Keycode.LEFT_ARROW], 0x000000, 'bck 1'),
        (0xFF0000, 'Scroll UP', [Keycode.SHIFT, ' '], 0x000000, 'scr up'),      # Scroll up
        (0xFF0000, 'Forward One Page', [Keycode.ALT, Keycode.RIGHT_ARROW], 0x000000, 'fwd 1'),
        (0xFF0000, 'Reload Current Page', [Keycode.CONTROL, 'r'], 0x000000, 'reload'),
        # 2nd row ----------
        (0xde0f62, 'Tab <', [Keycode.CONTROL, Keycode.PAGE_UP], 0x000000, 'tab lft'),
        (0xde0f62, 'Scroll Down', ' ', 0x000000, 'scr dwn'),                     # Scroll down
        (0xde0f62, 'Tab >', [Keycode.CONTROL, Keycode.PAGE_DOWN], 0x000000, 'tab rght'),
        (0xde0f62, 'PicNPic', [Keycode.CONTROL, Keycode.SHIFT, Keycode.RIGHT_BRACKET], 0x000000, 'pic win'),
        # 3rd row ----------
        (0xFFA500, 'New Private', [Keycode.CONTROL, Keycode.SHIFT, 'p'], 0x000000, 'new priv'),
        (0xFFA500, 'GitHub', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              'www.github.com\n'], 0x000000, 'GitHub'),  # github in new tab
        (0xFFA500, 'ASU', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'https://canvas.asu.edu/\n'], 0x000000, 'ASU'),     # canvas in new tab
        (0xFFA500, 'GPT', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'https://chat.openai.com/\n'], 0x000000, 'C.GPT'),     # ChatGPT in a new tab
        # Encoder button ---
        (0x000000, 'Close Window', [Keycode.CONTROL, 'w'], 0x000000, 'cls win')  # close firefox
    ]
}
