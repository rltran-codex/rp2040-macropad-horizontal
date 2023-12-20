from adafruit_hid.keyboard import Keycode
"""
Macropad Hotkey: Home Horizontal
Description:
Some macro hotkeys for my main day to day work flow and productivity.
If using Fancy Zone, make sure you set your top 3 favorite zones shortcut through PowerToys
"""

app = {
    'name': 'Home',  # Name of the macro
    'bmp': '',  # Path to .bmp image to display
    'animate': False,
    'macros': [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE   PRESSED COLOR  SHORT LABEL
        (0x9933ff, 'Open GitHub', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              'https://www.github.com\n'], 0x000000, 'GitHub'),
        (0x9933ff, 'Open Facebook Messenger', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              "https://www.facebook.com/messages\n"], 0x000000, 'F.MSG'),
        (0x9933ff, 'Open ChatGPT', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                              'https://chat.openai.com/\n'], 0x000000, 'CGPT'),
        (0x9933ff, 'Goto Page Right', [Keycode.CONTROL, Keycode.PAGE_DOWN], 0x000000, 'tab ->'),
        (0xFFFFFF, 'Fancy Zone 1', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.ALT,
                                    Keycode.ONE], 0x000000, '[fz_1]'),
        (0xFFFFFF, 'Fancy Zone 2', [
            Keycode.WINDOWS, Keycode.CONTROL, Keycode.ALT, Keycode.TWO], 0x000000, '[fz_2]'),
        (0xFFFFFF, 'Fancy Zone 3', [
            Keycode.WINDOWS, Keycode.CONTROL, Keycode.ALT, Keycode.THREE], 0x000000, '[fz_3]'),
        (0xFFFFFF, 'Goto Page Left', [Keycode.CONTROL, Keycode.PAGE_UP], 0x000000, 'tab <-'),
        (0xFF0000, 'Toggle Always On Top', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.T], 0x000000, 'onTop'),
        (0xFF0000, 'Spotify', [Keycode.WINDOWS, -Keycode.WINDOWS, "spotify", Keycode.ENTER], 0x000000, ''),
        (0xFF0000, 'Command Prompt', [Keycode.WINDOWS, -Keycode.WINDOWS, "cmd", Keycode.ENTER], 0x000000, 'cmd'),
        (0xFF0000, 'Discord Mute', [Keycode.RIGHT_ALT, Keycode.M], 0x000000, ''),

        (0x000000, '', [], 0x000000, '')  # encoder button
    ]
}
