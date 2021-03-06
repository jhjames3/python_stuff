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

# Pin Definitions
input_pin1 = 12 #18  # BCM pin 18, BOARD pin 12
input_pin2 = 13 

def main():
    prev_value1 = None
    prev_value2 = None
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin1, GPIO.IN)  # set pin as an input pin
    GPIO.setup(input_pin2, GPIO.IN)
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            value1 = GPIO.input(input_pin1)
            if value1 != prev_value1:
                if value1 == GPIO.HIGH:
                    value_str1 = "HIGH"
                    print("high")
                else:
                    value_str1 = "LOW"
                    print("low")
                print("Value read from pin {} : {}".format(input_pin1,
                                                           value_str1))
                prev_value1 = value1

            value2 = GPIO.input(input_pin2)
            if value2 != prev_value2:
                if value2 == GPIO.HIGH:
                    value_str2 = "HIGH"
                    print("high")
                else:
                    value_str2 = "LOW"
                    print("low")
                print("Value read from pin {} : {}".format(input_pin2,
                                                           value_str2))
                prev_value2 = value2
            time.sleep(1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
