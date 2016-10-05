# check dependency

try:
    import RPi.GPIO as GPIO
except:
    print("GPIO lib not found")

try:
    from lib_nrf24 import NRF24
except:
    print("lib_nrf24 library in not in the python path")

try:
    import spidev
except:
    print("py-spidev library not installed")

GPIO.setmode(GPIO.BCM)

radio = NRF24(GPIO,spidev.SpiDev())
radio.begin(0,17)

radio.setPayloadSize(32)
radio.setChannel(0x75)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()







