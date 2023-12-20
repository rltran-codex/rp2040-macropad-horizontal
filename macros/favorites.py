from adafruit_hid.keyboard import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
  'name' : 'Favorites',
  'bmp' : '/images/nyan_rainbow.bmp',
  'animate' : True,
  'macros' : [
    # 1st row ---------------
    (0xfda600, 'Virtual Desk LEFT', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.LEFT_ARROW], 0x00000, '< dsk '),
    (0xfda600, 'Virtual Desk ADD', [Keycode.COMMAND, Keycode.CONTROL, 'd'], 0x000000, '+ dsk'),
    (0xfda600, 'Virtual Desk RIGHT', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.RIGHT_ARROW], 0x00000, 'dsk >'),
    (0x0000ff, 'ChatGPT', [{'tone':200}, Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'https://chat.openai.com/\n'], 0x00cc99, 'C.GPT'),
    # 2nd row ---------------
    (0x0000ff, 'Tab LEFT', [Keycode.CONTROL, Keycode.PAGE_UP], 0x000000, '< TAB'),
    (0xfda600, 'Virtual Desk CLOSE', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.F4], 0x000000, '- dsk'),
    (0x0000ff, 'Tab RIGHT', [Keycode.CONTROL, Keycode.PAGE_DOWN], 0x000000, 'TAB >'),
    (0x0000ff, 'Facebook Messenger', [{'tone':200}, Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'https://www.facebook.com/messages\n'], 0x0866ff, 'FB.MSG'),
    # 3rd row ---------------
    (0x1c1b22, 'Fancy Zone 1', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.ALT, Keycode.ONE], 0x000000, '[fz_1]'),
    (0x1c1b22, 'Fancy Zone 2', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.ALT, Keycode.TWO], 0x000000, '[fz_2]'),
    (0x1c1b22, 'Fancy Zone 3', [Keycode.WINDOWS, Keycode.CONTROL, Keycode.ALT, Keycode.FOUR], 0x000000, '[fz_3]'),
    # ChatGPT in a new tab while using FireFox
    (0x5662f6, 'Discord Mute', [Keycode.RIGHT_ALT, 'm'], 0xff0000, 'Disc.M'),

    # encoder button
    (0x000000, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]], 0x000000,'Pau/P.')
  ]
}