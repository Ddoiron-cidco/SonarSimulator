import sys
import os
from serial import Serial
from time import sleep
from nmeasim.simulator import Simulator
ser = Serial('COM6')
ser.write_timeout = 0 # Do not block simulator on serial writing
sim = Simulator()
sim.serve(output=ser, blocking=False)
sleep(3)
sim.kill()

