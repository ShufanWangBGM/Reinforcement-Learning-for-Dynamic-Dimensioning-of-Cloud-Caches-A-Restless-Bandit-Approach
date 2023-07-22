import socket

# function used to load trace information
def loadID(Name):
    IDs = []
    TrRoot = "./Example/Traces/"
    Path = TrRoot + Name + ".csv"
    with open(Path) as fr:
        for f in fr:
            data =f[:-1].split(";")
            Id = int(data[1])
            IDs.append(Id)
    return IDs

# Proxy Server Information: IP + Port
ProxyIP = "http://0.0.0.0:8080/"

# Master Information
MasterIP = "127.0.0.1"
MasterPort = 5005

# Load Trace Information
RIDs = loadID("Bilibili")

# Implementation
address = (MasterIP, MasterPort)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(1024)
count = 0

while True:
    conn, addr = s.accept()
    send = ProxyIP + str(RIDs[count])
    conn.sendall(send.encode())
    count += 1
    print(count)