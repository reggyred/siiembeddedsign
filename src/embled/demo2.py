from controller import Controller
from effect import RainbowEffect

letter_d = 70
letter_e = 56
letter_m = 51
letter_b = letter_d

NO_OF_LEDS = letter_e + letter_m + letter_b + letter_e + letter_d + letter_d + letter_e + letter_d

effect = RainbowEffect(number_of_leds=NO_OF_LEDS, saturation=1.0, value=0.05, sleep_time=0.01)
controller = Controller(effect)
controller.start()
