import network  



wlan = network.WLAN(network.STA_IF)     #Objekt wlan als station interface

wlan.active(True)                       #System einschalten

if not wlan.isconnected():              #Wenn Wlan nicht verbunden ist -> 

    wlan.connect("BZTG-IoT", "WerderBremen24")      #Wlan verbinden

    while not wlan.isconnected():                   #Solange es nicht verbunden ist -> mache nichts

        pass

    print("Netzwerkkonfiguration: ", wlan.ifconfig())   #Netzwerkinfos ausgeben (IP Adresse, Subnetzmaske, Gateway, DNS-Server)