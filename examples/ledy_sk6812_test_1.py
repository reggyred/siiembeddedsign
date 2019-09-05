# This example does light up strip of 12 SK6812 LEDS
# Connections: 5V to pin 02, GND to pin 20, SPI MOSI (DIN) to pin 19.
import spidev
import time
from random import choice

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 7800000
HI = 0xF0
LO = 0xC0
ZEROS = 0x00

HI_ROW = [LO, LO, LO, HI, HI, HI, HI, HI] # we dont want full color brightness, just for testing
LO_ROW = [LO, LO, LO, LO, LO, LO, LO, LO] # all low bits

def mix(one, two, three):
    data=[]
    data.extend(one)
    data.extend(two)
    data.extend(three)
    return data

green = mix(HI_ROW, LO_ROW, LO_ROW)
red = mix(LO_ROW, HI_ROW, LO_ROW)
blue = mix(LO_ROW, LO_ROW, HI_ROW)

colors = [red, green, blue]

# lets send 10 sets of 12 random colors
for _ in range(10):
    data = []
    # create list of 12 random of red, blue and green
    for _ in range(12):
       data.extend(choice(colors))
    # send 12 colors (12 x 3 bytes)
    spi.xfer3(data)
    # send 100 zeros to generate reset signal (sign that transfer has ended)
    data = [ZEROS]*100
    spi.xfer3(data)
    time.sleep(1)