import time
import urllib.request
import socket

# Configuration of Master: IP, Port
MasterIP = "127.0.0.1"
MasterPort = 5005

Break = 0
# Client ID
ClientID = 1
while Break == 0:
    # get requested content ID from Master
    Url = "http://"
    try:
        address = (MasterIP, MasterPort)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        trigger = str(ClientID)
        s.sendall(trigger.encode())
        data = s.recv(1024)
        data = data.decode()
        s.close()
        Url = data
    except:
        continue

    # send request to Proxy Server
    try:
        response = urllib.request.urlopen(Url)
        html = response.read()
        print(Url,"Done...")
    except:
        print("Invalid Request...")
        continue

