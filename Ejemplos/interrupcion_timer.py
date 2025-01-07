import machine, time
from machine import Pin, Timer

#Configuracion Pin
led = Pin(2, Pin.OUT,value=0)

#Funcion de interrupcion
def interrupcion():
    led(not led()) #Toggle

#Declaracion de la interrupcion
#callback especifica la funcion a ejecutar
#Set timer a 1sg/1000ms
Timer(0).init(period=1000, mode=Timer.PERIODIC, callback=lambda t:interrupcion())

#Main
while True:
    pass