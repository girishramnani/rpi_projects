import RPi.GPIO as GPIO
from lib_nrf24 import NRF24

import time
import spidev

GPIO.setmode(GPIO.BCM)

pipes =[[0xE8,0xe8,0xF0,0xF0,0xE1],[0xF0,0xF0,0xF0,0xF0,0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())

radio.begin(0,17)

radio.setPayloadSize(32)

radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1,pipes[1])
radio.printDetails()
radio.startListening()


while True:
    while not radio.available(0):
        time.sleep(1/100)
    receivedMessage = []
    print(radio.getDynamicPayloadSize())
    radio.read(receivedMessage, radio.getDynamicPayloadSize())

    decoded_message ="".join(map(lambda asci : chr(asci),receivedMessage))
    print("Received: {}".format(decoded_message))


