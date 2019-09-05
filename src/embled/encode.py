from bitstring import BitArray


def encode_rgb(rgb_data, limit):
    """Converts data in RGB format to corresponding SPI values
    Args:
        rgb_data - list of color data RGB (0-255)
        limit - safety limiter for brightness, defines how many bits are in fact used (from right)

    Returns:
        encoded colors ready to be transmitted with SPI
    """
    hi = 0xF0
    lo = 0xC0
    out = []
    safety = 8 - limit
    for item in rgb_data:
        encoded_led = []
        for index, bit in enumerate(BitArray(uint=item.green, length=8)):
            if bit and index >= safety:
                encoded_led.append(hi)
            else:
                encoded_led.append(lo)
        for bit in BitArray(uint=item.red, length=8):
            if bit and index >= safety:
                encoded_led.append(hi)
            else:
                encoded_led.append(lo)
        for bit in BitArray(uint=item.blue, length=8):
            if bit and index >= safety:
                encoded_led.append(hi)
            else:
                encoded_led.append(lo)
        out.extend(encoded_led)
    return out

def encode_simple(in_data, limit):
    hi = 0xF0
    lo = 0xC0
    
    on = [lo, lo, lo, lo, lo, lo, hi, hi]
    off = [lo, lo, lo, lo, lo, lo, lo, lo]
    red = off + on + off
    blue = off + off + on
    
    data = []
    for item in in_data:
        if item == 1:
            data.extend(red)
        elif item == 2:
            data.extend(blue)
    return data
