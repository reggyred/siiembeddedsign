from colors import RGB
from led_driver import LedDriver
import numpy
from colorsys import hsv_to_rgb
from time import sleep
import collections


def generate_rainbow(number):
    data = []
    h = 0.0
    for i in range(number):
        r, g, b = hsv_to_rgb(h, 1.0, 0.1)
        data.append(RGB(r, g, b))
        h += 1.0/number
        if h > 1:
            h = 0.0
    return data


def rotate_list(lst, n):
    d = collections.deque(lst)
    d.rotate(n)
    return list(d)


NO_OF_LEDS = 55
driver = LedDriver()
source = generate_rainbow(NO_OF_LEDS)

try:
    while True:
        for n in range(NO_OF_LEDS):
            data = rotate_list(source, n)
            driver.transmit(data)
            sleep(1.0/120)
except KeyboardInterrupt:
    pass
