# import serial
# import RPi.GPIO as GPIO
#import datetime

# arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(21, GPIO.OUT)
#GPIO.setwarnings(FALSE)
#mot_start='$'
#mot_stop='&'

"""

 commented out the gpi stuff because i dont have raspy now

"""

import sys
import random
import string
import threading
from mainUi import *

def generate_random_data():

    return "".join([random.choice(string.ascii_letters) for _ in range(10)])

def your_code(window):
    " you have the access to the window object inside of this block"
    while True:
        







application = QApplication(sys.argv)

window = MainWindow(application)
thread = threading.Thread(target=lambda : your_code(window))
thread.setDaemon(True)
thread.start()
window.show()

application.exec_()

while True:
    #print 'LED KING'
    print("Sdf")

        #GPIO.output(21,False)
        #for i in range (30000):
        #    print 'low'
        #else:
        
        #if(myData == "Motor On"):
         #  if (myData == mot_start):
        #GPIO.output(21,True)
        #for i in range (30000):
        #    print 'high'

        #tyme = datetime.datetime.now()
        #print tyme

        #textfile = open ("pyth1.txt",'a')
        #textfile.write(myData)
        #textfile.write(",")
        #textfile.write(str(tyme)+"\n,")
        #textfile.close()
