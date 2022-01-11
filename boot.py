import network
import usocket as socket

ssid = 'esp32_Baum'         #Netzwerkname
passwort = 'Baum1997'       #Passwort       

ap = network.WLAN(network.AP_IF)    #AccesspointInterface
ap.active(True)                     #aktivieren
ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password = passwort) #Konfiguration

print(ap.ifconfig()) #Netzwerkinfo ausgeben



ap_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ap_socket.bind(('', 80))

ap_socket.listen(5)

while True:

    con, adr = ap_socket.accept()

    print("Anfrage von IP-Adresse {0}".format(str(adr)))

    request = con.recv(1024)

    con.send('HTTP/1.1 200 OK\n')

    con.send('Content-Type: text/html\n')

    con.send('Connection: close\n\n')

    response = "<h1><span style=\"color: #ff0000;\"><strong>Hello World!</strong></span></h1>"

    con.sendall(response)

    con.close()


