# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
A macro/hotkey program for Adafruit MACROPAD. Macro setups are stored in the
/macros folder (configurable below), load up just the ones you're likely to
use. Plug into computer's USB port, use dial to select an application macro
set, press MACROPAD keys to send key sequences and other USB protocols.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import time
import displayio
import terminalio
from rainbowio import colorwheel
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from adafruit_ticks import ticks_ms, ticks_add, ticks_less


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/macros'
SLEEP_TIMER = 50 * 60 * 1000  # 50 min
# SLEEP_TIMER = 5000 # for testing
FRAME_RATE = 150  # 200 ms
HINTS_TRIGGER = 3
# CLASSES AND FUNCTIONS ----------------


class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""

    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']
        self.bmp_path = None
        self.isAnimation = False
        try:
            self.bmp_path = appdata['bmp']
            self.isAnimation = appdata['animate']
        except KeyError:
            print("no bmp found for " + self.name)

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[1].text = add_newline(self.name, 10)   # Application name
        group[2].text = ""  # area to display activated macro
        self.remove_img()  # remove current image
        self.add_img()  # add current image

        for i in range(12):
            if i < len(self.macros):  # Key in use, set LED color
                macropad.pixels[i] = self.macros[i][0]
            else:  # Key not in use, no LED
                macropad.pixels[i] = 0
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()

    def add_img(self):
        """
        add image onto the display group;
        should be added at the end
        """
        if self.bmp_path:
            try:
                img_bmp = displayio.OnDiskBitmap(open(self.bmp_path, 'rb'))
                img_tilegrid = displayio.TileGrid(
                    img_bmp, pixel_shader=displayio.ColorConverter(), x=7, y=39)
                group.append(img_tilegrid)
                macropad.display.refresh()
            except Exception as e:
                print(e)
                pass

    def remove_img(self):
        try:
            group.pop(3)
        except IndexError:
            pass
        macropad.display.refresh()

    def animate(self):
        """
        Move the image on the x horizontal.
        """
        if (self.isAnimation):
            try:
                if group[3].x > 64:
                    group[3].x = -50
                else:
                    group[3].x += 1

                if group[3].x % 2 == 0:
                    group[3].y += 4
                else:  # group[3].x % 2 == 0:
                    group[3].y -= 4

                macropad.display.refresh()
            except IndexError:
                pass

    def toggle_hints(self, trigger: bool):
        if (trigger):
            hint_group = displayio.Group()
            hint_group.append(Rect(0, 0, macropad.display.width, macropad.display.height, fill=0xFFFFFF))
            # Add labels to the group in list manner
            for key_index in range(13):
                text = ""
                try:
                    if key_index < 10:
                        text = f' {key_index}: {self.macros[key_index][4]}'
                    else:
                        text = f'{key_index}: {self.macros[key_index][4]}'
                except:
                    text = f'{key_index}: null'
                hint_group.append(label.Label(terminalio.FONT, text=text, color=0x000000,
                                              anchored_position=(
                                                  0, (key_index + 1) * 10),
                                              anchor_point=(0, 1.0)))

            macropad.display.root_group = hint_group
        else:
            macropad.display.root_group = group
        macropad.display.refresh()

    def disp_macro_pressed(self, idx):
        if idx < len(self.macros):
            self.remove_img()
            group[2].text = self.macros[idx][1].replace(" ", "\n")
        else:
            group[2].text = ''
            if (self.bmp_path):
                self.add_img()
        macropad.display.refresh()


class Sleeper:

    def __init__(self):
        self.key_colors = [0.0, 21.25, 42.5, 63.75, 85.0, 106.25, 127.5, 148.75,
                           170.0, 191.25, 212.5, 233.75]  # Initialize key colors for each pixel
        self.sleep_timer = ticks_add(ticks_ms(), SLEEP_TIMER)

    def sleep_macropad(self, curr_app: App):
        if not (self.sleep_ready()):
            return

        curr_app.remove_img()
        group[1].text = "LOCKED"
        group[2].text = "Unlock.by.pressing.any key.twice".replace(
            ".", "\n")
        macropad.display.refresh()
        wake_count = 0
        DISPLAY_SLEEP = 30000
        disp_sleep = ticks_add(ticks_ms(), DISPLAY_SLEEP)

        while True:
            for i in range(12):
                self.key_colors[i] = (self.key_colors[i] - 0.75) % 255
                macropad.pixels[i] = colorwheel(self.key_colors[i])
                macropad.pixels.show()

            key_event = macropad.keys.events.get()
            if key_event:
                if (macropad.display_sleep == False and key_event.pressed):
                    wake_count += 1
                macropad.display_sleep = False
                macropad.pixels.brightness = 100
                disp_sleep = ticks_add(ticks_ms(), DISPLAY_SLEEP)

            if wake_count == 2:
                curr_app.switch()
                self.push_sleep()
                break

            if (ticks_less(disp_sleep, ticks_ms())):
                if macropad.pixels.brightness > .35:
                    macropad.pixels.brightness -= .005
                wake_count = 0
                macropad.display_sleep = True

    def sleep_ready(self) -> bool:
        return ticks_less(self.sleep_timer, ticks_ms())

    def push_sleep(self):
        self.sleep_timer = ticks_add(ticks_ms(), SLEEP_TIMER)


def add_newline(input_string, max_line_length):
    result = ""
    current_length = 0

    for char in input_string:
        result += char
        current_length += 1

        # Check if the current length exceeds the maximum line length
        if current_length >= max_line_length:
            result += '\n'
            current_length = 0

    return result


def init_main_group():
    g = displayio.Group()
    g.append(Rect(0, 0, macropad.display.width, 26, fill=0xFFFFFF))
    g.append(label.Label(terminalio.FONT, text='', color=0x000000,
                         anchored_position=(macropad.display.width//2, -1),
                         anchor_point=(0.5, 0.0)))
    macro_label = label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                              anchored_position=(
                                  macropad.display.width/2, macropad.display.height / 2),
                              anchor_point=(0.5, 0.5))
    g.append(macro_label)
    return g


def handle_hints(param : tuple):
    h_on = param[0]
    hk_cnt = param[1]
    timer = param[2]

    if h_on and ticks_less(timer, ticks_ms()):
        h_on = False
        apps[app_index].toggle_hints(h_on)

    if hk_cnt == HINTS_TRIGGER :
        h_on = True
        timer = ticks_add(ticks_ms(), 10000)
        apps[app_index].toggle_hints(h_on)
        hk_cnt = 0
    
    return h_on, hk_cnt, timer

# INITIALIZATION -----------------------
macropad = MacroPad(rotation=270)
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False
# Set up displayio group with all the labels
group = init_main_group()
macropad.display.root_group = group

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py') and not filename.startswith('._'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    group[2].text = 'NO MACRO FILES FOUND'.replace(" ", "\n")
    macropad.display.refresh()
    while True:
        pass

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()

# timer and trigger for displaying macro label
disp_macro_timer = 0
disp_macro = False

sleep_lock = Sleeper()                           # Sleep and lock object
frame_timer = ticks_add(ticks_ms(), FRAME_RATE)  # rate to do animation

hints_hotkey = 0
hints_timer = 0
hints_on = False

print("Horizontal Pad Initialized")
# MAIN LOOP ----------------------------
while True:
    # handle hints window
    hints_on, hints_hotkey, hints_timer = handle_hints((hints_on, hints_hotkey, hints_timer))

    # handle animation window
    if ticks_less(frame_timer, ticks_ms()):
        apps[app_index].animate()
        frame_timer = ticks_add(ticks_ms(), FRAME_RATE)

    # handle macro label pressed
    if ((ticks_less(disp_macro_timer, ticks_ms()))) and disp_macro:
        apps[app_index].disp_macro_pressed(404)
        disp_macro = False

    # Read encoder position. If it's changed, switch apps.
    position = macropad.encoder
    if position != last_position:
        sleep_lock.push_sleep()
        app_index = position % len(apps)
        apps[app_index].switch()
        last_position = position
        # hints_on = True
        # hints_hotkey = 0
        # hints_timer = ticks_add(ticks_ms(), 2000)
        # apps[app_index].toggle_hints(True)

    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        if len(apps[app_index].macros) < 13:
            continue    # No 13th macro, just resume main loop
        key_number = 12  # else process below as 13th macro
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            # put display to sleep if sleep_timer has caught up
            sleep_lock.sleep_macropad(apps[app_index])
            continue  # No key events, or no corresponding macro, resume loop
        hints_hotkey = 0
        sleep_lock.push_sleep()
        key_number = event.key_number
        pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    sequence = apps[app_index].macros[key_number][2]

    if pressed:
        if key_number == 12:
            hints_hotkey += 1
        # 'sequence' is an arbitrary-length list, each item is one of:
        # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
        # Negative integer: (absolute value) key released
        # Float (e.g. 0.25): delay in seconds
        # String (e.g. "Foo"): corresponding keys pressed & released
        # List []: one or more Consumer Control codes (can also do float delay)
        # Dict {}: mouse buttons/motion (might extend in future)
        if key_number < 12:  # No pixel for encoder button
            try:
                macropad.pixels[key_number] = apps[app_index].macros[key_number][3]
            except:
                macropad.pixels[key_number] = 0xe534eb
            macropad.pixels.show()
        apps[app_index].disp_macro_pressed(key_number)
        disp_macro_timer = ticks_add(ticks_ms(), 2000)
        disp_macro = True
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.press(item)
                else:
                    macropad.keyboard.release(-item)
            elif isinstance(item, float):
                time.sleep(item)
            elif isinstance(item, str):
                macropad.keyboard_layout.write(item)
            elif isinstance(item, list):
                for code in item:
                    if isinstance(code, int):
                        macropad.consumer_control.release()
                        macropad.consumer_control.press(code)
                    if isinstance(code, float):
                        time.sleep(code)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.press(item['buttons'])
                    else:
                        macropad.mouse.release(-item['buttons'])
                macropad.mouse.move(item['x'] if 'x' in item else 0,
                                    item['y'] if 'y' in item else 0,
                                    item['wheel'] if 'wheel' in item else 0)
                if 'tone' in item:
                    if item['tone'] > 0:
                        macropad.stop_tone()
                        macropad.start_tone(item['tone'])
                    else:
                        macropad.stop_tone()
                elif 'play' in item:
                    macropad.play_file(item['play'])
    else:
        # Release any still-pressed keys, consumer codes, mouse buttons
        # Keys and mouse buttons are individually released this way (rather
        # than release_all()) because pad supports multi-key rollover, e.g.
        # could have a meta key or right-mouse held down by one macro and
        # press/release keys/buttons with others. Navigate popups, etc.
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    macropad.keyboard.release(item)
            elif isinstance(item, dict):
                if 'buttons' in item:
                    if item['buttons'] >= 0:
                        macropad.mouse.release(item['buttons'])
                elif 'tone' in item:
                    macropad.stop_tone()
        macropad.consumer_control.release()
        if key_number < 12:  # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
