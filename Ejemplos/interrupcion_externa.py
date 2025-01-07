import machine, time
from machine import Pin

#Pin de salida
led = Pin(2, Pin.OUT)

#Pines de entrada con PULL_UP
boton = Pin(18, Pin.IN, Pin.PULL_UP)

#Funcion de interrupcion
def interrupcion(pin):
    led(not led()) #Toggle
    time.sleep_ms(100) #Delay 100ms

#Declaracion de la interrupcion
#Handler especifica la funcion a ejecutar
#Trigger especifica el modo de activacion
boton.irq(handler=interrupcion, trigger=Pin.IRQ_FALLING)

#Main
while True:
    pass