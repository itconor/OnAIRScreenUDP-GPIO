import RPi.GPIO as GPIO
from time import sleep
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

data = ("AIR1:ON")
data2 = ("AIR1:OFF")
datas = [data2, data]
lastst = None

while True:
    sleep(.4)
    newst = GPIO.input(17)
    if newst == lastst:
        continue
    lastst = newst
    client_socket.sendto(datas[newst], ("127.0.0.1", 3310))
