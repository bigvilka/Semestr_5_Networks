import socket

MULTICAST_TTL = 1 
MULTICAST = 'multicast'
MULTICAST_IP = '224.1.1.1'
BROADCAST = 'broadcast'
BROADCAST_IP = '255.255.255.255'
UNICAST = 'unicast'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

def send(mode):
    UDP_IP_DST = ''
    if mode == BROADCAST:
        UDP_IP_DST = BROADCAST_IP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    if mode == MULTICAST:
        UDP_IP_DST = MULTICAST_IP
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        loop_back = input("Loopback on? (y/n): ")
        if loop_back == 'y':
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        if loop_back == 'n':
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)
    if mode == UNICAST:
        UDP_IP_DST = str(input('Enter distination ip: '))
    while True:
        msg = str(input('Message: '))
        sock.sendto(bytes(msg, "utf-8"), (UDP_IP_DST, UDP_DST_PORT))


UDP_DST_PORT = int(input('Enter distination port: '))
print("Choose unicast, multicast, broadcast.")
mode = str(input("Enter mode: ")).lower()
send(mode)