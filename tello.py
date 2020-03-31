import threading 
import socket
import sys

class Tello:
    def __init__(self):
        self.tello_host = '192.168.10.1'
        self.tello_port = 8889
        self.local_host = ''
        self.local_port = 9000
        self.tello_address = (self.tello_host, self.tello_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.local_host, self.local_port))
        
    def send(self, command):
        try:
            self.sock.sendto(command.encode(encoding="utf-8"), self.tello_address)
            print("Sending command: " + command)
        except Exception as e:
            print("Send error: " + str(e))
            
    def receive(self):
        try:
            response, ip = self.sock.recvfrom(128)
            print(response.decode(encoding='utf-8') + " from Tello with IP: " + str(ip))
        except Exception as e:
            print("Receive error: " + str(e))

    def close(self):
        self.socket.close()
    
        
        
