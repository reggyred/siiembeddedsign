import abc
import collections
from colorsys import hsv_to_rgb
from time import sleep

from colors import RGB
from encode import encode_rgb


def rotate_list(lst, n):
    d = collections.deque(lst)
    d.rotate(n)
    return list(d)


class Effect(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def generate(self):
        pass


class RainbowEffect(Effect):
    def __init__(self, number_of_leds, saturation=1.0, value=0.05, sleep_time=0.01):
        self.sleep = sleep_time
        self.data = self.raw_rainbow(number_of_leds, saturation, value)

    @staticmethod
    def raw_rainbow(number_of_leds, saturation, value):
        rainbow_data = []
        h = 0.0
        for i in range(number_of_leds):
            r, g, b = hsv_to_rgb(h, saturation, value)
            rainbow_data.append(RGB(r, g, b))
            h += 1.0 / number_of_leds
            if h > 1:
                h = 0.0
        source_rgb = encode_rgb(rainbow_data, 8)
        return collections.deque(source_rgb)

    def generate(self):
        sleep(self.sleep)
        self.data.rotate(24)  # rotate 24 bits
        return list(self.data)


class ColorToWhiteEffect(Effect):
    def __init__(self, number_of_leds, color, value=0.05, sleep_time=0.01):
        self.sleep = sleep_time
        self.data = self.color_to_white(number_of_leds, color, value)

    @staticmethod
    def color_to_white(number_of_leds, color, value):
        saturation = 1.0
        saturation_range = []
        saturation_increment = saturation/(number_of_leds-1)
        for i in range(number_of_leds):
            saturation.append(i*saturation_increment)
        color_data = []
        for i in range(number_of_leds):
            r, g, b = hsv_to_rgb(color, saturation_range[i], value)
            color_data.append(RGB(r, g, b))
            h += 1.0 / number_of_leds
            if h > 1:
                h = 0.0
        source_rgb = encode_rgb(color_data, 8)
        return collections.deque(source_rgb)

    def generate(self):
        sleep(self.sleep)
        self.data.rotate(24)  # rotate 24 bits
        return list(self.data)

