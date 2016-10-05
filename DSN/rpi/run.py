from dep import *
import time
import signal
import sys

def term_handler(_signo,_stack_frame):
    print(_signo,"Exiting ..")
    sys.exit(0)

signal.signal(signal.SIGINT,term_handler)
signal.signal(signal.SIGTERM,term_handler)




pipes = [[0xE7,0xE8,0xF0,0xF0,0xE1],[0xF0,0xF0,0xF0,0xF0,0xE1]]

radio.openReadingPipe(1,pipes[1])
radio.printDetails()
radio.startListening()

while True:
    
    while not radio.available(0):
        time.sleep(1/100)
    receivedMessage = []
    readio.read(receivedMessage,radio.getDynamicPayloadSize())
    print("Received: {}".format(receivedMessage))

    decodedM = []
    for char in receivedMessage:
        if char >=32 and char <=126:
            decodedM.append(chr(char))
    print("Decoded Message : {}".format("".join(decodedM)))



