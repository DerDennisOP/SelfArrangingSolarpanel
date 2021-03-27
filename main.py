from lcdrgb import TFT
from machine import Pin, SPI
from sysfont import sysfont
import time
import math

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

d = TFT(spi, 12, 13, 14)
d.initr()
d.rgb(True)
#d.on()
#d.pixel((10,10), d.color(255, 0, 0))
def testlines(color):
    d.fill(d.BLACK)
    for x in range(0, d.size()[0], 6):
        d.line((0,0),(x, d.size()[1] - 1), color)
    for y in range(0, d.size()[1], 6):
        d.line((0,0),(d.size()[0] - 1, y), color)

    d.fill(d.BLACK)
    for x in range(0, d.size()[0], 6):
        d.line((d.size()[0] - 1, 0), (x, d.size()[1] - 1), color)
    for y in range(0, d.size()[1], 6):
        d.line((d.size()[0] - 1, 0), (0, y), color)

    d.fill(d.BLACK)
    for x in range(0, d.size()[0], 6):
        d.line((0, d.size()[1] - 1), (x, 0), color)
    for y in range(0, d.size()[1], 6):
        d.line((0, d.size()[1] - 1), (d.size()[0] - 1,y), color)

    d.fill(d.BLACK)
    for x in range(0, d.size()[0], 6):
        d.line((d.size()[0] - 1, d.size()[1] - 1), (x, 0), color)
    for y in range(0, d.size()[1], 6):
        d.line((d.size()[0] - 1, d.size()[1] - 1), (0, y), color)

def testfastlines(color1, color2):
    d.fill(d.BLACK)
    for y in range(0, d.size()[1], 5):
        d.hline((0,y), d.size()[0], color1)
    for x in range(0, d.size()[0], 5):
        d.vline((x,0), d.size()[1], color2)

def testdrawrects(color):
    d.fill(d.BLACK);
    for x in range(0,d.size()[0],6):
        d.rect((d.size()[0]//2 - x//2, d.size()[1]//2 - x/2), (x, x), color)

def testfillrects(color1, color2):
    d.fill(d.BLACK);
    for x in range(d.size()[0],0,-6):
        d.fillrect((d.size()[0]//2 - x//2, d.size()[1]//2 - x/2), (x, x), color1)
        d.rect((d.size()[0]//2 - x//2, d.size()[1]//2 - x/2), (x, x), color2)


def testfillcircles(radius, color):
    for x in range(radius, d.size()[0], radius * 2):
        for y in range(radius, d.size()[1], radius * 2):
            d.fillcircle((x, y), radius, color)

def testdrawcircles(radius, color):
    for x in range(0, d.size()[0] + radius, radius * 2):
        for y in range(0, d.size()[1] + radius, radius * 2):
            d.circle((x, y), radius, color)

def testtriangles():
    d.fill(d.BLACK);
    color = 0xF800
    w = d.size()[0] // 2
    x = d.size()[1] - 1
    y = 0
    z = d.size()[0]
    for t in range(0, 15):
        d.line((w, y), (y, x), color)
        d.line((y, x), (z, x), color)
        d.line((z, x), (w, y), color)
        x -= 4
        y += 4
        z -= 4
        color += 100

def testroundrects():
    d.fill(d.BLACK);
    color = 100
    for t in range(5):
        x = 0
        y = 0
        w = d.size()[0] - 2
        h = d.size()[1] - 2
        for i in range(17):
            d.rect((x, y), (w, h), color)
            x += 2
            y += 3
            w -= 4
            h -= 6
            color += 1100
        color += 100

def dprinttest():
    d.fill(d.BLACK);
    v = 30
    d.text((0, v), "Hello World!", d.RED, sysfont, 1, nowrap=True)
    v += sysfont["Height"]
    d.text((0, v), "Hello World!", d.YELLOW, sysfont, 2, nowrap=True)
    v += sysfont["Height"] * 2
    d.text((0, v), "Hello World!", d.GREEN, sysfont, 3, nowrap=True)
    v += sysfont["Height"] * 3
    d.text((0, v), str(1234.567), d.BLUE, sysfont, 4, nowrap=True)
    time.sleep_ms(1500)
    d.fill(d.BLACK);
    v = 0
    d.text((0, v), "Hello World!", d.RED, sysfont)
    v += sysfont["Height"]
    d.text((0, v), str(math.pi), d.GREEN, sysfont)
    v += sysfont["Height"]
    d.text((0, v), " Want pi?", d.GREEN, sysfont)
    v += sysfont["Height"] * 2
    d.text((0, v), hex(8675309), d.GREEN, sysfont)
    v += sysfont["Height"]
    d.text((0, v), " Print HEX!", d.GREEN, sysfont)
    v += sysfont["Height"] * 2
    d.text((0, v), "Sketch has been", d.WHITE, sysfont)
    v += sysfont["Height"]
    d.text((0, v), "running for: ", d.WHITE, sysfont)
    v += sysfont["Height"]
    d.text((0, v), str(time.ticks_ms() / 1000), d.PURPLE, sysfont)
    v += sysfont["Height"]
    d.text((0, v), " seconds.", d.WHITE, sysfont)

def test_main():
    d.fill(d.BLACK)
    d.text((0, 0), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", d.WHITE, sysfont, 1)
    time.sleep_ms(1000)

    dprinttest()
    time.sleep_ms(4000)

    testlines(d.YELLOW)
    time.sleep_ms(500)

    testfastlines(d.RED, d.BLUE)
    time.sleep_ms(500)

    testdrawrects(d.GREEN)
    time.sleep_ms(500)

    testfillrects(d.YELLOW, d.PURPLE)
    time.sleep_ms(500)

    d.fill(d.BLACK)
    testfillcircles(10, d.BLUE)
    testdrawcircles(10, d.WHITE)
    time.sleep_ms(500)

    testroundrects()
    time.sleep_ms(500)

    testtriangles()
    time.sleep_ms(500)

test_main()

# from time import sleep_ms, ticks_ms
# from machine import I2C, Pin
# from lcd import I2cLcd

# def test_main():
#     """Test function for verifying basic functionality."""
#     print("Running test_main")
#     i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
#     lcd = I2cLcd(i2c, 0x27, 4, 20)
#     lcd.putstr("It Works!\nSecond Line")
#     sleep_ms(3000)
#     lcd.clear()
#     count = 0
#     while True:
#         lcd.move_to(0, 0)
#         lcd.putstr("%7d" % (ticks_ms() // 1000))
#         sleep_ms(1000)
#         count += 1
#         if count % 10 == 3:
#             print("Turning backlight off")
#             lcd.backlight_off()
#         if count % 10 == 4:
#             print("Turning backlight on")
#             lcd.backlight_on()
#         if count % 10 == 5:
#             print("Turning display off")
#             lcd.display_off()
#         if count % 10 == 6:
#             print("Turning display on")
#             lcd.display_on()
#         if count % 10 == 7:
#             print("Turning display & backlight off")
#             lcd.backlight_off()
#             lcd.display_off()
#         if count % 10 == 8:
#             print("Turning display & backlight on")
#             lcd.backlight_on()
#             lcd.display_on()
#             lcd.putstr("It Works!\nSecond Line")