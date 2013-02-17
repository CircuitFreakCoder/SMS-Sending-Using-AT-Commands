'''
Sending SMS using AT Commands
'''

import serial
import time

#function for sending
def Sending(message, sender):
    SerialPort = serial.Serial("COM7",115200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS="'+sender+'"\r\n')
    time.sleep(1)
    SerialPort.write(message+"\x1A")
    time.sleep(1)
    print 'message sent'

x = raw_input("type the number: \n")
y = raw_input("type the message: \n")

Sending(y,x)

