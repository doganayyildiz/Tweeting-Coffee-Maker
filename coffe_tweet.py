import network
import urequests
from time import sleep
from machine import Pin
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ssid","password")
sleep(5)
print(wlan.isconnected())

buton= Pin(14,Pin.IN,Pin.PULL_DOWN)
counter = 2

while True:
    if buton.value():
        counter +=1
        print(counter)
        sleep(0.5)
        message= "https://maker.ifttt.com/trigger/Post_Tweet/with/key/apikey"+str(counter)
        urequests.post(message)
        sleep(3600)
