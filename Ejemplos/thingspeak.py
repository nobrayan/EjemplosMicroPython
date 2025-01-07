import machine, network, time, urequests 
from machine import Pin, ADC

#Configuracion thingspeak
HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'KEY'

UPDATE_TIME_INTERVAL = 1000  # en ms
last_update = time.ticks_ms() 

#Configuracion WiFi
WiFi = network.WLAN(network.STA_IF)
if not WiFi.isconnected():
    WiFi.active(True)
    WiFi.connect('SSD', 'PASS')
    print('Conectando a la red...')
    while not WiFi.isconnected():
        pass
print('CONFIGURACION DE RED (IP/MASCARA/GATEWAY/DNS):', WiFi.ifconfig())

#Pines de Lectura
pin1 = ADC(Pin(34, Pin.IN))
pin2 = ADC(Pin(35, Pin.IN))
pin3 = ADC(Pin(32, Pin.IN))

while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
        
        #Lecturas
        lectura1 = pin1.read()
        lectura2 = pin2.read()
        lectura3 = pin3.read()

        esp_readings = {'field1':lectura1, 'field2':lectura2, 'field3':lectura3, 'field4':lectura4} #Dato a entregar 
        request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = esp_readings, headers = HTTP_HEADERS )  
        request.close() 
        print(esp_readings)