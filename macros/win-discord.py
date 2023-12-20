from adafruit_hid.keycode import Keycode

"""
MacroPad Discord macros
  Manually added shortcuts in disc
  - Toggle Mute : RIGHT ALT + M
  - Push to Mute : RIGHT ALT + .
  - Toggle Screen Share : ALT + CTRL + SHIFT + S
  - Disconnect from VC : RIGHT ALT + CTRL + SHIFT + /
  - Toggle Deafen : RIGHT ALT + RIGHT SHIFT + M
"""
app = {
  'name' : 'Discord',
  'bmp' : '/images/discord_logo.bmp',
  'animate' : False,
  'macros' : [
    # (COLOR, LABEL, KEY SEQUENCE, PRESS COLOR, SHORT LABEL)
    # 1st row
    (0x5662f6, 'Channel UP', [Keycode.ALT, Keycode.UP_ARROW], 0xFFFFFF, 'C.UP'),
    (0x5662f6, 'Server UP', [Keycode.CONTROL, Keycode.ALT, Keycode.UP_ARROW], 0xFFFFFF, 'S.UP'),
    (0x5662f6, 'Mark Channel as READ', [Keycode.ESCAPE], 0xFFFFFF, 'C.READ'),
    (0x5662f6, '', [], 0x000000, ''),
    # 2nd row
    (0x5662f6, 'Channel DOWN', [Keycode.ALT, Keycode.DOWN_ARROW], 0xFFFFFF, 'C.DWN'),
    (0x5662f6, 'Server DOWN', [Keycode.CONTROL, Keycode.ALT, Keycode.DOWN_ARROW], 0xFFFFFF, 'S.DWN'),
    (0x5662f6, 'Mark Server as READ', [Keycode.SHIFT, Keycode.ESCAPE], 0xFFFFFF, 'S.READ'),
    (0x5662f6, '', [], 0x000000, ''),
    # 3rd row
    (0xff695e, 'Screen Share', [Keycode.ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.S], 0xFFFFFF, 'scrn shr'),
    (0xff695e, 'Toggle Mute', [Keycode.RIGHT_ALT, Keycode.M], 0x5662f6, 'T.Mute'),
    (0xff695e, 'Push to Mute', [Keycode.RIGHT_ALT, Keycode.PERIOD], 0x5662f6, 'P.Mute'),
    (0xff695e, 'Toggle Deafen', [Keycode.RIGHT_ALT, Keycode.RIGHT_SHIFT, Keycode.M], 0x5662f6, 'T.Deaf'),
    # Encoder button
    (0x5662f6, 'Disconnect from Voice Channel', [Keycode.RIGHT_ALT, Keycode.CONTROL, Keycode.SHIFT, Keycode.BACKSLASH], 0x000000, 'dc vc')
  ]
}