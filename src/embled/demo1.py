from colors import RGB
from led_driver import LedDriver
from colorsys import hsv_to_rgb
from time import sleep
import collections
from encode import encode_rgb


def generate_rainbow(number):
    data = []
    h = 0.0
    for i in range(number):
        r, g, b = hsv_to_rgb(h, 1.0, 0.05)
        data.append(RGB(r, g, b))
        h += 1.0/number
        if h > 1:
            h = 0.0
    return data


def rotate_list(lst, n):
    d = collections.deque(lst)
    d.rotate(n)
    return list(d)


letter_e_cripple = 53
letter_d = 70
letter_e = 56
letter_m = 51
letter_b = letter_d

NO_OF_LEDS = letter_e + letter_m + letter_b + letter_e + \
        + letter_d + letter_d + letter_e + letter_d

driver = LedDriver()
source = generate_rainbow(NO_OF_LEDS)
source_rgb = encode_rgb(source, 8)

try:
    while True:
        for n in range(0, NO_OF_LEDS*24, 24):
            data = rotate_list(source_rgb, n)
            driver.transmit_no_encode(data)
            driver.reset_signal()
            sleep(0.01)
except KeyboardInterrupt:
    pass
