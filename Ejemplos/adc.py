import machine, time
from machine import Pin, ADC

#Pin de entrada ADC
lectura = ADC(Pin(34, Pin.IN))

#Main
while True:
    consola = lectura.read() #Lectura ADC1 Pin 34
    print(consola) #Impresion en consola
    time.sleep_ms(500) #Delay 500ms