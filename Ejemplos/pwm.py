import machine, time
from machine import Pin, PWM

#Pin de salida PWM
pwm = PWM(Pin(2, Pin.OUT))

#Configuracion de frecuencia PWM
pwm.init(freq=60)

#Main
while True:
    #Aumentar
    for i in range(0, 1024):
        pwm.duty(i) #Cambio del Duty (Ciclo de Trabajo)
        time.sleep_ms(1) #Delay 1ms
        
    #Decrecer
    for i in range(1023, 0, -1):
        pwm.duty(i) #Cambio del Duty (Ciclo de Trabajo)
        time.sleep_ms(1) #Delay 1ms