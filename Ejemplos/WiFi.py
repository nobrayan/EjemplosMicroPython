import network

#Conexion WiFi
WiFi = network.WLAN(network.STA_IF)
if not WiFi.isconnected():
    WiFi.active(True)
    WiFi.connect("SSID", "CONTRASEÑA")
    print("Conectando a la red...")
    while not WiFi.isconnected():
        pass

print("CONFIGURACION DE RED (IP/MASCARA/GATEWAY/DNS):", WiFi.ifconfig())