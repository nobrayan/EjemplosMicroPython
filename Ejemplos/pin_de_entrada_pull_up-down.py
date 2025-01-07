import machine, time
from machine import Pin

#Numero del Pin
numero_pin = 4

#Pin de entrada
#Entrada configurada a PULL_UP, cambiar a PULL_DOWN si desea ingresar 3.3v
pin = Pin(numero_pin, Pin.IN, Pin.PULL_UP)

#Main
while True:
    consola = pin.value() #Obtener el valor de pin
    print(f'Valor Pin{numero_pin}: {consola}') #Impresion en consola
    time.sleep_ms(500) #Delay de 500ms