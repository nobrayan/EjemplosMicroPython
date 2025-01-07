import machine, time, network, socket
from machine import Pin

#Conexion WiFi
led_connection = Pin(2, Pin.OUT, value = 0)
WiFi = network.WLAN(network.STA_IF)
if not WiFi.isconnected():
    WiFi.active(True)
    WiFi.connect("SSID", "PASS")
    print("Conectando a la red...")
    while not WiFi.isconnected():
        led_connection.value(1)
        time.sleep(.1)
        led_connection.value(0)
        time.sleep(.1)
        pass
led_connection.value(1)
print("CONFIGURACION DE RED (IP/MASCARA/GATEWAY/DNS):", WiFi.ifconfig())

#Variables
led = Pin(4, Pin.OUT, value = 0)
led_state, led_icon = "APAGADO", ""
boton_on, boton_off = "btn btn-outline-success", "btn btn-outline-danger active"

#Pagina web
def web_page():  
    html = """
<html>
    <head>
        <title>PRUEBA ESP32</title>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    </head>

    <body style="margin:5%;padding:0">
        <div class="container d-grid gap-3" align="center">
            <div class="card" style="width: 18rem">
                <i class="bi bi-lightbulb""" + led_icon + """ " style="font-size: 250; margin:5%;padding:0"></i>
                <div class="card-body">
                    <h5 class="card-text">LED</h5>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item text-muted">ESTADO: """ + led_state + """</li>
                </ul>
                <div class="card-body">
                    <a class=" """ + boton_on + """ " href="/led=on" role="button">ON</a>
                    <a class=" """ + boton_off + """ " href="/led=off" role="button">OFF</a>
                </div>
            </div>
        </div>
    </body>
</html>    """
    return html

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(("", 80))
tcp_socket.listen(1)

while True:
    conn, addr = tcp_socket.accept()
    #print("Nueva conexion desde: %s" % str(addr))
    request = conn.recv(1024)
    #print("Solicitud = %s" % str(request))
    request = str(request)
    
    #Funciones
    if request.find("/led=on") == 6:
        led.value(1)
        led_state, led_icon = "ENCENDIDO", "-fill"
        boton_on, boton_off = "btn btn-outline-success active", "btn btn-outline-danger"
        
    if request.find("/led=off") == 6:
        led.value(0)
        led_state, led_icon = "APAGADO", ""
        boton_on, boton_off = "btn btn-outline-success", "btn btn-outline-danger active"
    
    #Mostrar Página
    response = web_page()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-Type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()