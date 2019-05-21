# This example does light up strip of 8 WS2812 LEDS with basic colors.
# WS2812 have different timings than SK6812, so SPI clock and bytes values used
# to mock hi-low signal ratio should be adjusted.
# Connections: 5V to pin 02, GND to pin 20, SPI MOSI (DIN) to pin 19.

import spidev
import time
from random import shuffle

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 7800000
HI = 0xF8
LO = 0xE0
HI_ROW = [LO, LO, LO, HI, HI, HI, HI, HI]
LO_ROW = [LO, LO, LO, LO, LO, LO, LO, LO]

def mix(one, two, three):
    data=[]
    data.extend(one)
    data.extend(two)
    data.extend(three)
    return data

red = mix(HI_ROW, LO_ROW, LO_ROW)
green = mix(LO_ROW, HI_ROW, LO_ROW)
blue = mix(LO_ROW, LO_ROW, HI_ROW)

data=[]
data.extend(red)
data.extend(green)
data.extend(blue)
data.extend(red)
data.extend(blue)
data.extend(green)
data.extend(red)
data.extend(blue)

spi.xfer3(data)
   
