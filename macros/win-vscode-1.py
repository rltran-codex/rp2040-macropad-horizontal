from adafruit_hid.keyboard import Keycode
"""
MACROPAD Hotkeys for VSCode. 
Easier navigation around and other useful tools quite frequently I use in the text editor.
Designed to act like a mini keyboard while using VSCode
"""
vs_code_short = [Keycode.CONTROL, Keycode.K]

app = {
    'name': 'VS Code - MAIN',
    'bmp' : '/images/vscode_logo.bmp',
    'animate' : False,
    'macros': [
        # 1st row ---------------
        (0x0099ff, 'Page LEFT', [Keycode.CONTROL, Keycode.PAGE_UP], 0x000000, 'pg <-'),
        (0x6600ff, 'UP', [Keycode.UP_ARROW], 0x000000, 'crsr ^'),
        (0x0099ff, 'Page RIGHT', [Keycode.CONTROL, Keycode.PAGE_DOWN], 0x000000, 'pg ->'),
        (0xffcc00, 'Focus Explorer Tab', [Keycode.SHIFT, Keycode.CONTROL, 'E'], 0x000000, 'xplr tab'),
        # 2nd row ---------------
        (0x6600ff, 'LEFT', [Keycode.CONTROL, Keycode.LEFT_ARROW], 0x000000, 'crsr <-'),
        (0x6600ff, 'DOWN', [Keycode.DOWN_ARROW], 0x000000, 'crsr v'),
        (0x6600ff, 'RIGHT', [Keycode.CONTROL, Keycode.RIGHT_ARROW], 0x000000, 'crsr ->'),
        (0xffcc00, 'References', [Keycode.SHIFT, Keycode.F12], 0xff6699, 'refs'),
        # 3rd row ---------------
        (0x666699, 'Collapse Subregion', vs_code_short + \
         [Keycode.CONTROL, Keycode.LEFT_BRACKET], 0x000000, 'fold'),
        (0x666699, 'Uncollapse Subregion', vs_code_short + \
         [Keycode.CONTROL, Keycode.RIGHT_BRACKET], 0x000000, 'unfold'),
        (0xffcc00, 'Format Document', [Keycode.SHIFT, Keycode.ALT, 'f'], 0xff6699, 'F.Doc'),
        (0xffcc00, 'Reveal in Folder Explorer', vs_code_short + [-Keycode.CONTROL, -Keycode.K, Keycode.R], 0x000000, 'fldr'),

        # encoder button
        (0xFF0000, 'Enter', [Keycode.ENTER], 0x000000, '->|')
    ]
}
