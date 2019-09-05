from colors import RGB
from led_driver import LedDriver
import numpy
from colorsys import hsv_to_rgb
from time import sleep

driver = LedDriver()

h = 0.0

point1 = RGB(127, 0, 0)
point2 = RGB(0, 127, 0)
point3 = RGB(0, 0, 127)
blank = RGB(1, 1, 1)
source = [point1, point2, point3, blank, blank, blank, blank, blank, blank, blank, blank, blank]
try:
    while True:
        data = []
        for i in range(12):
            data.extend(source[i:12])
            data.extend(source[0:i])
            driver.transmit(data)
        sleep(1/10)
except KeyboardInterrupt:
    pass
