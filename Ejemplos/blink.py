import time
from machine import Pin

#Numero de Pin
pin_led = 2 #Cambiar el numero del Pin a elección

#Pin de salida
led = Pin(pin_led, Pin.OUT)

#Main
while True:
    led.on()
    time.sleep_ms(500) #Delay 500ms
    led.off()
    time.sleep_ms(500) #Delay 500ms