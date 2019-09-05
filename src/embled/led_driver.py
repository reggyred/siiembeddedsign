<<<<<<< HEAD
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
=======
import spidev
from encode import encode_rgb
from time import time

class LedDriver:

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 7800000

    def reset_signal(self):
        data = [0x00] * 200
        self.spi.xfer3(data)

    def transmit(self, data, encode_func=encode_rgb, limit=8):
        t0 = time()
        print("Starting encoding")
        out = encode_func(data, limit=limit)
        t1 = time()
        print("Encoding took: {}".format(t1-t0))
        print("Starting sending")
        self.spi.xfer3(out)
        t2 = time()
        print("Sending took: {}".format(t2-t1))
        print("Starting reset")
        self.reset_signal()
        t3 = time()
        print("Reset took: {}".format(t3-t2))

    def transmit_part(self, data, encode_func=encode_rgb, limit=8):
        out = encode_func(data, limit=limit)
        self.spi.xfer2(out)

>>>>>>> WIP1
