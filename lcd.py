from machine import I2C
import time

class LCD():

    def __init__(self, i2c, address, rows, cols):
        self.i2c = i2c
        self.address = address
        self.rows = rows
        self.cols = cols
        
        self.backlightMode = 0x00;
        self.begin()


    def begin(self):
        # _displayfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS;
        #

        # wait for display init after power-on
        time.sleep_ms(50) # 50ms

        self.send(0)
        time.sleep_ms(1000)


    def backlight(self, on):
        if on:
            self.backlightMode = 0x08;
        else:
            self.backlightMode = 0x00;
        self.send(0)

    def send(self, value):
        self.i2c.writeto(self.address, bytearray([(value) | self.backlightMode]))



from machine import Pin, I2C

i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
d = LCD(i2c,39,4,20)
d.backlight(True)
time.sleep_ms(1000);
d.backlight(False)
