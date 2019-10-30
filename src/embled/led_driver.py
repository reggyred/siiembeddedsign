import spidev
from encode import encode_rgb


class LedDriver:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 7800000

    def reset_signal(self):
        data = [0x00] * 200
        self.spi.xfer3(data)

    def transmit(self, data, encode_func=encode_rgb, limit=8):
        out = encode_func(data, limit=limit)
        self.spi.xfer3(out)
        self.reset_signal()

    def transmit_no_encode(self, data):
        self.spi.xfer3(data)
        self.reset_signal()

    def transmit_part(self, data, encode_func=encode_rgb, limit=8):
        out = encode_func(data, limit=limit)
        self.spi.xfer2(out)
