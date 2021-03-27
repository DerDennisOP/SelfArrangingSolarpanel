import display.i2c_lcd as lcd
from machine import Pin, I2C

i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
d = lcd.Display(i2c)

d.home()
d.write('Hello World')
