import socket,os,ipaddress,threading,time

def attempt_connect(port,address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.05)
    if sock.connect_ex((address,port)) == 0:
        #print(str(port)+" is open")
        sock.close()
        open_ports.append(port)
    else:
        #print(str(port)+" is closed")
        sock.close()
        return False

def attempt_ping(address):
    if os.system("ping -n 1 -c 1 "+address) == 0:
        #print(str(address)+" is online")
        online.append(address)
    else:
        #print(str(address)+" is offline")
        pass

if (input("enter (ip) for ip address scan, otherwise (any) for port scan:")=='ip'):
    addresses = input("address range:")

    online = []
    for address in ipaddress.IPv4Network(addresses):
        threading.Thread(target=attempt_ping,args=[str(address)]).start()
        while threading.active_count()>50:
            time.sleep(0.1)
    print(online)
else:
    address = input("scan target address")
    start = int(input("start port:"))
    end = int(input("end port:"))

    open_ports = []
    for port in range(start,end+1):
        threading.Thread(target=attempt_connect,args=[port,address]).start()
        while threading.active_count()>10:
            time.sleep(0.1)
    print(open_ports)
