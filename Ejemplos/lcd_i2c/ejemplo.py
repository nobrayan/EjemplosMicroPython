import machine, time
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

battery_0 = [0x0E,
  0x1B,
  0x11,
  0x11,
  0x11,
  0x11,
  0x11,
  0x1F]
battery_15 = [0x0E,
  0x1B,
  0x11,
  0x11,
  0x11,
  0x11,
  0x1F,
  0x1F]
battery_30 = [  0x0E,
  0x1B,
  0x11,
  0x11,
  0x11,
  0x1F,
  0x1F,
  0x1F]
battery_45 = [0x0E,
  0x1B,
  0x11,
  0x11,
  0x1F,
  0x1F,
  0x1F,
  0x1F]
battery_60 = [0x0E,
  0x1B,
  0x11,
  0x1F,
  0x1F,
  0x1F,
  0x1F,
  0x1F]
battery_75 = [0x0E,
  0x1B,
  0x1F,
  0x1F,
  0x1F,
  0x1F,
  0x1F,
  0x1F]
battery_100 = [0x0E,
  0x1F,
  0x1F,
  0x1F,
  0x1F,
  0x1F,
  0x1F,
  0x1F]

def lcd_str(mensaje, fila, columna):
    lcd.move_to(fila, columna)
    lcd.putstr(mensaje)

#Caracter personalizado
lcd.custom_char(0, bytearray(battery_0))
lcd.custom_char(1, bytearray(battery_15))
lcd.custom_char(2, bytearray(battery_30))
lcd.custom_char(3, bytearray(battery_45))
lcd.custom_char(4, bytearray(battery_60))
lcd.custom_char(5, bytearray(battery_75))
lcd.custom_char(6, bytearray(battery_100))

#Main
while True:
    lcd.clear()
    lcd_str("Bateria:", 4, 0)
    lcd.move_to(4,1)
    for i in range(0,7):
        lcd.putchar(chr(i))
    time.sleep(3)
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Ejemplo LCD 16x2")
    time.sleep(1)
    lcd.move_to(0,1)
    lcd.putstr("      CON")
    time.sleep(1)
    lcd_str("      I2C       ", 0, 0)
    time.sleep(1)
    lcd_str("     ESP32      ", 0, 1)
    time.sleep(1)
    
    lcd.clear()
    lcd_str("Numeros en", 3, 0)
    lcd_str("Esquinas", 4, 1)
    time.sleep(1)
    
    lcd_str("1", 0, 0)
    time.sleep(1)
    lcd_str("2", 15, 0)
    time.sleep(1)
    lcd_str("3", 0, 1)
    time.sleep(1)
    lcd_str("4", 15, 1)
    time.sleep(1)
    
    #Cursor
    lcd.clear()
    lcd_str("LCD I2C", 0, 0)
    lcd_str("Activar: Cursor", 0, 1)
    lcd.blink_cursor_on()
    time.sleep(2)
    
    #Backspace
    for j in range(1, -1, -1):
        for i in range(14, -1, -1):
            lcd.move_to(i, j)
            lcd.putstr(' ')
            lcd.move_to(i, j)
            time.sleep_ms(100)
    time.sleep(1)
    lcd.hide_cursor()
    
    #BackLight
    lcd.clear()
    lcd.backlight_off()
    lcd_str("BackLight: OFF", 0, 0)
    time.sleep(3)
    
    lcd.clear()
    lcd.backlight_on()
    lcd_str("BackLight: ON", 0, 0)
    time.sleep(3)