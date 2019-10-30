from led_driver import LedDriver


class Controller:
    def __init__(self, effect):
        self.driver = LedDriver()
        self.effect = effect

    def start(self):
        try:
            while True:
                data = self.effect.generate()
                self.driver.transmit_no_encode(data)
                self.driver.reset_signal()
        except KeyboardInterrupt:
            pass

    def stop(self):
        pass
