import socket 
import struct

MULTICAST = 'multicast'
MULTICAST_IP = '224.1.1.1'
BROADCAST = 'broadcast'
UNICAST = 'unicast'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

def recieve(mode):
    UDP_IP_SENDER = ''
    if mode == BROADCAST:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    if mode == MULTICAST:
        UDP_IP_SENDER = MULTICAST_IP
        r = struct.pack("4sl", socket.inet_aton(UDP_IP_SENDER), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, r)
    if mode == UNICAST:
        UDP_IP_SENDER = str(input('Enter sender ip: '))
    sock.bind((UDP_IP_SENDER, UDP_SENDER_PORT))
    while True:
        data, addr = sock.recvfrom(1024) 
        print("message: ", str(data, encoding='utf-8'))


UDP_SENDER_PORT = int(input('Enter sender port: '))
print("Choose unicast, multicast or broadcast.")
mode = str(input("Enter mode: ")).lower()
recieve(mode)