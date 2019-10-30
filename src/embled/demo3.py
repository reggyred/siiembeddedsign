<<<<<<< HEAD
from colors import RGB
from led_driver import LedDriver
import numpy
from colorsys import hsv_to_rgb
from time import sleep

driver = LedDriver()

h = 0.0

try:
    while True:
        data = []
        for i in range(60):
            r, g, b = hsv_to_rgb(h, 1.0, 0.3)
            data.append(RGB(r, g, b))
            h += 0.02
            if h > 1:
                h = 0.0
        driver.transmit(data)
        sleep(3)
except KeyboardInterrupt:
    pass
=======
from colors import RGB
from led_driver import LedDriver
import numpy
from colorsys import hsv_to_rgb
from time import sleep

driver = LedDriver()

h = 0.0

try:
    while True:
        data = []
        for i in range(60):
            r, g, b = hsv_to_rgb(h, 1.0, 0.3)
            data.append(RGB(r, g, b))
            h += 0.02
            if h > 1:
                h = 0.0
        driver.transmit(data)
        sleep(3)
except KeyboardInterrupt:
    pass
>>>>>>> WIP1
