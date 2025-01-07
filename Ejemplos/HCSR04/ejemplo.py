import machine, time, HCSR04
from machine import Pin, Timer

period = 100
maxDevice = 4
sensor = HCSR04.HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=500*2*30)

def timerEvent():
    distance = int(sensor.distance_cm())
    lectura = 24 - distance
    if(lectura <= 0):
        lectura = 0
    print("Distancia: ", lectura, " cm")
    time.sleep(.5)
 
Timer(1).init(period=period, mode=Timer.PERIODIC, callback=lambda t: timerEvent())

while True:
    pass 
