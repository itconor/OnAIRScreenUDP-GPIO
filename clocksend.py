import RPi.GPIO as GPIO
import time
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

data = ("AIR1:ON")
data2 = ("AIR1:OFF")

try:
    while True:
        if GPIO.input(17) == True:
            client_socket.sendto(data, ("127.0.0.1",3310))
            time.sleep(.4)
        else:
            client_socket.sendto(data2, ("127.0.0.1",3310))
        time.sleep(.4)

except KeyboardInterrupt:  
    GPIO.cleanup()         # clean up after yourself  
