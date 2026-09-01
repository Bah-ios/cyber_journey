import socket

def scan():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ### AF_INET  means use IPV4 and SOCK_STREAM  means use TCP 
    port = int(input("Enter the port you want to scan: "))
    try:
        s.connect(("localhost", port))
        print("open")
    except ConnectionRefusedError:
        print("closed")
for i in range(5):
    scan()