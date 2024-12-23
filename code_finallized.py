# Lab 02 - Group 1X
# Name: XXX, YYY
# SID: 5XXXXXXX, 5XXXXXXX

import random
import time
import music
from microbit import *

pin0.set_pull(pin0.PULL_DOWN)
pin1.set_pull(pin1.PULL_DOWN)
pin2.set_pull(pin2.PULL_DOWN)

# Returns a picture from microbit built-in class
def random_pictures():
    """Returns a random picture from microbit built-in class"""
    try:
        # Getting all images
        images = [Image.__dict__[i] for i in Image.__dict__ if isinstance(Image.__dict__[i], Image) and Image.__dict__[i] != Image.YES and Image.__dict__[i] != Image.NO]
        return random.choice(images)
    except RuntimeError:
        return Image.SKULL    # Return something

class MagicSwitchboard:
    def __init__(self):
        self.switch_to_led = {}    # Initialization

    # Logging the switches during initialization
    def switch_init(self):
        """Logging the switches with their corresponding LED light bulb"""
        if self.switch_to_led != {}:
            self.switch_to_led = {}    # Initialization
        # Mapping switches (buttons) to LEDs using string names
        while not len(self.switch_to_led) >= 3:    # There are 3 switches in total
            # Turn on all LEDs to lead to confusion
            if pin13.read_digital() and "pin13" not in self.switch_to_led:  # Button 13 pressed (pulled to GND)
                if len(self.switch_to_led) == 0:
                    self.switch_to_led["pin13"] = "pin0"
                    pin0.write_digital(1)
                    sleep(200)
                    pin0.write_digital(0)
                elif len(self.switch_to_led) == 1:
                    self.switch_to_led["pin13"] = "pin1"
                    pin1.write_digital(1)
                    sleep(200)
                    pin1.write_digital(0)
                else:
                    self.switch_to_led["pin13"] = "pin2"
                    pin2.write_digital(1)
                    sleep(200)
                    pin2.write_digital(0)

            if pin14.read_digital() and "pin14" not in self.switch_to_led:  # Button 14 pressed (pulled to GND)
                if len(self.switch_to_led) == 0:
                    self.switch_to_led["pin14"] = "pin0"
                    pin0.write_digital(1)
                    sleep(200)
                    pin0.write_digital(0)
                elif len(self.switch_to_led) == 1:
                    self.switch_to_led["pin14"] = "pin1"
                    pin1.write_digital(1)
                    sleep(200)
                    pin1.write_digital(0)
                else:
                    self.switch_to_led["pin14"] = "pin2"
                    pin2.write_digital(1)
                    sleep(200)
                    pin2.write_digital(0)
            
            if pin15.read_digital() and "pin15" not in self.switch_to_led:  # Button 15 pressed (pulled to GND)
                if len(self.switch_to_led) == 0:
                    self.switch_to_led["pin15"] = "pin0"
                    pin0.write_digital(1)
                    sleep(200)
                    pin0.write_digital(0)
                elif len(self.switch_to_led) == 1:
                    self.switch_to_led["pin15"] = "pin1"
                    pin1.write_digital(1)
                    sleep(200)
                    pin1.write_digital(0)
                else:
                    self.switch_to_led["pin15"] = "pin2"
                    pin2.write_digital(1)
                    sleep(200)
                    pin2.write_digital(0)
        return

    # Toggle the RGB lights - determined by sound level
    def sound_level_detector(self):
        """Toggle the RGB lights by sound level"""
        display.show(Image.YES)
        time.sleep(0.5)
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
        while not pin_logo.is_touched():
            if microphone.sound_level() <= 70:
                display.show("0", wait=False)
                # Turn off all LEDs
                pin0.write_digital(0)
                pin1.write_digital(0)
                pin2.write_digital(0)
            if microphone.sound_level() > 70:
                # Turn on the left LED
                display.show("1", wait=False)
                pin0.write_digital(1)
                pin1.write_digital(0)
                pin2.write_digital(0)
            if microphone.sound_level() > 180:
                # Turn on the left LED and the middle LED
                display.show("2", wait=False)
                pin0.write_digital(1)
                pin1.write_digital(1)
                pin2.write_digital(0)
            if microphone.sound_level() > 225:
                # Turn on all LEDs
                display.show("3", wait=False)
                pin0.write_digital(1)
                pin1.write_digital(1)
                pin2.write_digital(1)
            time.sleep(0.1)
        return

    # Function to convert a string pin name to the actual pin object
    def get_pin(self, pin_name):
        """Convert a string pin name to the actual pin object."""
        pin_map = {
            "pin0": pin0,
            "pin1": pin1,
            "pin2": pin2,
            "pin3": pin3,
            "pin4": pin4,
            "pin5": pin5,
            "pin6": pin6,
            "pin7": pin7,
            "pin8": pin8,
            "pin9": pin9,
            "pin10": pin10,
            "pin11": pin11,
            "pin12": pin12,
            "pin13": pin13,
            "pin14": pin14,
            "pin15": pin15,
            "pin16": pin16,
            "pin19": pin19,
            "pin20": pin20
        }
        return pin_map.get(pin_name)
    
    # Function to play some music
    def music_box(self):
        """Play some music"""
        # Play Marry have a little lamb
        music.play(["E4:3", "D4:3", "C4:3", "D4:3", "E4:3", "E4:3", "E4:6", 
                    "D4:3", "D4:3", "D4:6", "E4:3", "G4:3", "G4:6", 
                    "E4:3", "D4:3", "C4:3", "D4:3", "E4:3", "E4:3", "E4:6", 
                    "D4:3", "D4:3", "E4:3", "D4:3", "C4:6"], 
                   wait=False, pin=None)

        # Pin toggling sequence fine-tuned to the song's rhythm
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin0.write_digital(1)
        sleep(350)
        pin0.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(800)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin1.write_digital(1)
        sleep(750)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(1350)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin0.write_digital(1)
        sleep(350)
        pin0.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(800)
        pin2.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin1.write_digital(1)
        sleep(350)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(350)
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(800)
        pin1.write_digital(0)
        pin0.write_digital(1)
        sleep(800)
        pin0.write_digital(0)

    # Update the RGB LED light bulbs status
    def update_leds(self):
        """Update the RGB LED light bulbs status"""
        # Check each switch and set the corresponding LED state based on the switch state
        for switch_name, led_name in self.switch_to_led.items():
            switch_pin = self.get_pin(switch_name)
            led_pin = self.get_pin(led_name)
            
            if switch_pin is None or led_pin is None:
                continue
            # If the switch is pressed (pin reads 0), turn on the LED, otherwise turn it off
            if switch_pin.read_digital():  # Button pressed (pulled to GND)
                led_pin.write_digital(1)  # Turn on LED
            else:
                led_pin.write_digital(0)  # Turn off LED
        return
            
switchboard = MagicSwitchboard()

# Run the program asynchronously
def asynchronous_run(seconds):
    """Run the program as a 'couroutine'"""
    end_time = time.ticks_add(time.ticks_ms(), int(seconds * 1000))
    reset = True
    display.show(random_pictures())
    while time.ticks_diff(end_time, time.ticks_ms()) > 0:
        switchboard.update_leds()
        if accelerometer.is_gesture("shake"):
            switchboard.sound_level_detector()
        if button_b.is_pressed() or pin_logo.is_touched():
            # Check if both buttons are pressed
            time.sleep(0.1)
            if button_a.is_pressed():
                #raise NotImplementedError("Unsupported opeartion for pressing both buttons simultaneously.")
                switchboard.music_box()
                reset = False
            return reset    # Terminates the program
        # Check if any button is pressed and cancel the reset if so
        if pin13.read_digital() or pin14.read_digital() or pin15.read_digital():
            reset = False
    return reset

# Callback for function main()
def after_serving():
    """Callback for function main()"""
    music.play(music.BA_DING, pin=None, wait=False)
    display.show(Image('09000:99990:09009:00009:99990:'))    # Custom back arrow
    terminate = button_b.is_pressed()
    if terminate:    # Terminates the program
        display.show(Image.NO)
    time.sleep(1)
    display.clear()
    if not terminate:
        main()   # Call main to soft reset
    return

# Main function
def main():
    """Main program loop"""
    display.on()
    while not button_a.is_pressed():
        sleep(0.001)
        if button_b.is_pressed() or pin_logo.is_touched():
            break
    if button_a.is_pressed():
        switchboard.switch_init()
    while button_a.was_pressed:
        if asynchronous_run(5):
            break
    after_serving()    # callback
# For 1st time startup only
if __name__ == "__main__":
    # The following executes for the 1st time only
    music.play(music.NYAN, pin=None, wait=False)
    display.scroll("Press A to start, tap the logo to reset, or press B to stop.", delay=60)
    main()

