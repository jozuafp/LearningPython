# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 13:36:00 2021

@author: Jozua Palandi
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

while (True):
    GPIO.output(14, True)
    time.sleep(1)
    GPIO.output(14, False)
    time.sleep(1)
    