import machine, time
from machine import Pin

#Pin de salida
pin = Pin(2, Pin.OUT)

#Main
pin.value(1) #Valor de pin en 1
time.sleep(1) #Delay de 1sg
pin.value(0) #Valor de pin en 0