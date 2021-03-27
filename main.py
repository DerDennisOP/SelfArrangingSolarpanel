from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from lcd import I2cLcd

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    # On the RPi Pico, I2C0 shows up on GP8 (sda) and GP9 (scl)
    i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
    lcd = I2cLcd(i2c, 0x, 4, 20)
    lcd.putstr("It Works!\nSecond Line")
    sleep_ms(3000)
    lcd.clear()
    count = 0
    while True:
        lcd.move_to(0, 0)
        lcd.putstr("%7d" % (ticks_ms() // 1000))
        sleep_ms(1000)
        count += 1
        if count % 10 == 3:
            print("Turning backlight off")
            lcd.backlight_off()
        if count % 10 == 4:
            print("Turning backlight on")
            lcd.backlight_on()
        if count % 10 == 5:
            print("Turning display off")
            lcd.display_off()
        if count % 10 == 6:
            print("Turning display on")
            lcd.display_on()
        if count % 10 == 7:
            print("Turning display & backlight off")
            lcd.backlight_off()
            lcd.display_off()
        if count % 10 == 8:
            print("Turning display & backlight on")
            lcd.backlight_on()
            lcd.display_on()
            lcd.putstr("It Works!\nSecond Line")

test_main()