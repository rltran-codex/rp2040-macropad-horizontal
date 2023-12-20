from adafruit_hid.keyboard import Keycode
"""
MACROPAD Hotkeys for VSCode, in the terminal.
Executing git actions.
"""
app = {
  'name' : 'VS Code - GIT',
  'bmp' : '/images/github_logo.bmp',
  'animate' : False,
  'macros' : [
    # 1st row
    (0xc9510c, 'git init', ['git init'], 0x000000, 'init'),
    (0xc9510c, 'Integrated Terminal', [Keycode.CONTROL, Keycode.J], 0x000000, 'trml'),
    (0xc9510c, 'add all tracked file', ['git add . \n'], 0x000000, 'add .'),
    (0xc9510c, 'commit', ['git commit -m ""', Keycode.LEFT_ARROW], 0x000000, 'status'),
    # 2nd row
    (0x6e5494, 'Pull', ['git pull\n', Keycode.LEFT_ARROW], 0x000000, 'pull'),
    (0x6e5494, 'Main pull', ['git pull origin main\n'], 0x000000, 'm.pull'),
    (0x6e5494, 'Push', ['git push\n'], 0x000000, 'push'),
    (0x6e5494, 'Add Remote', ['git remote add origin '], 0x000000, '+rmte'),
    # 3rd row
    (0x333, 'Change to main branch',  ['git checkout main\n'], 0x000000, 'M.Br'),
    (0x333, 'Checkout branch',   ['git checkout -b '], 0x000000, 'CO.Br'),
    (0x333, 'Rename branch', ['git checkout -M '], 0x000000, 'Rnme.Br'),
    (0x333, 'Open GitHub', ['start firefox https://github.com/', Keycode.ENTER], 0x000000, 'GitHub'),

    # Encoder button
    (0x000000, '', [], 0x000000, 'n')
  ]
}