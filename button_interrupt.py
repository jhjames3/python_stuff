#!/usr/bin/env python

# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import Jetson.GPIO as GPIO
import time

# Pin Definitions:
led_pin_1 = 12
led_pin_2 = 13
#but_pin = 18

# blink LED 2 quickly 5 times when button pressed
def blink1(channel):
    print(channel)
    print(" Blink LED 1 up")
    print("Value read from pin {} : {}".format(led_pin_1, '1up'))

    

def blink2(channel):
    pring(channel)
    print("Blink LED 2 up")
    print("Value read from pin {} : {}".format(led_pin_2, '2up'))
    

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    # GPIO.setup([led_pin_1, led_pin_2], GPIO.IN)  # LED pins set as output
    GPIO.setup(led_pin_1, GPIO.IN)  # button pin set as input
    #GPIO.setup(led_pin_2, GPIO.IN)

    # Initial state for LEDs:
    # GPIO.output(led_pin_1, GPIO.LOW)
    # GPIO.output(led_pin_2, GPIO.LOW)

    GPIO.add_event_detect(led_pin_1, GPIO.RISING, callback=blink1, bouncetime=10)
    #GPIO.add_event_detect(led_pin_2, GPIO.RISING, callback=blink2, bouncetime=10)

    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:

            input1 = GPIO.input(led_pin_1)
            #input2 = GPIO.input(led_pin_2)
            # blink LED 1 slowly
            print("Value read from pin {} : {}\n".format(input1, '1down'))
            time.sleep(2)
            #print("Value read from pin {} : {}\n".format(input2, '2down'))
            time.sleep(1)
    finally:
        GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    main()
