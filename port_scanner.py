import socket

def scan():
    starting_port = int(input("Enter the port you want to scan or the staring range "))
    dest_port = int(input("Enter Destination port"))

    for port in range(starting_port,dest_port+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ### AF_INET  means use IPV4 and SOCK_STREAM  means use TCP 
        try:
            s.connect(("localhost", port))
            print("port {} is Open".format(port))
        except ConnectionRefusedError:
            print("Port {} is closed".format(port))
            
scan()