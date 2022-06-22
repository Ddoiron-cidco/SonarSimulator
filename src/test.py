import sys
import os
import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 4800)
ser.open()
ser.write(b'hello')
ser.close()

'''
ser.write_timeout = 0 # Do not block simulator on serial writing
sim = Simulator()
sim.serve(output=ser, blocking=False)
sleep(3)
sim.kill()
'''
