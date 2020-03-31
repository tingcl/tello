from tello import Tello
import time

def main():
    tello = Tello()
    while True:
        try:
            command = input(">")
            if(command == 'end'):
                tello.close() 
                break
            else:
                tello.send(command)
                tello.receive()
                time.sleep(1)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            tello.close() 
            break

main()
