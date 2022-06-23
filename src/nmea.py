'''
# Copyright 2022 © Centre Interdisciplinaire de développement en Cartographie des Océans (CIDCO), Tous droits réservés
@Jacob Bellavance

'''
import sys
import os
import time
from datetime import datetime
from pprint import pprint
from nmeasim.models import TZ_LOCAL
from nmeasim.simulator import Simulator
import math
import threading
import time
from random import random
from sys import stdout


DURATION = 1

###### Main #########################
def checkSum(data):
    sum=0
    for ch in data:
        sum^=ord(ch)
    return f'{data}*{sum:02X}'


if len(sys.argv) > 1:
    # Open simulator and output file
    simulator = Simulator()
    serialPort = open("/dev/ttyUSB0", "w")

#    with sim.lock:

    #Generate GGA
    # Can re-order or drop some
#    sim.gps.output = tuple()
    simulator.gps.output = ('GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA')
    simulator.gps.num_sats = 14
    simulator.gps.lat = 1
    simulator.gps.lon = 3
    simulator.gps.altitude = -13
    simulator.gps.geoid_sep = -45.3
    simulator.gps.mag_var = -1.1
    simulator.gps.kph = 60.0
    simulator.gps.heading = 90.0
    simulator.gps.mag_heading = 90.1
    simulator.gps.date_time = datetime.now(TZ_LOCAL)  # PC current time, local time zone
    simulator.gps.hdop = 3.1
    simulator.gps.vdop = 5.0
    simulator.gps.pdop = (simulator.gps.hdop ** 2 + simulator.gps.vdop ** 2) ** 0.5
    # Precision decimal points for various measurements
    simulator.gps.horizontal_dp = 4
    simulator.gps.vertical_dp = 1
    simulator.gps.speed_dp = 1
    simulator.gps.time_dp = 2
    simulator.gps.angle_dp = 1
    # Keep straight course for simulator - don't randomly change the heading
    simulator.heading_variation = 0
    #simulator.generate(3, serialPort)
    while True :
        simulator.generate(DURATION, serialPort)
        #for sentence in simulator.get_output(DURATION):
            #simulator.generate(DURATION,serialPort)
            #print(type(sentence))
            #serialPort.write(sentence)
            #time.sleep(1)
          # serialPort.write('\r\n')
         
    # Generate DBT
        depthMeters = 42.0 #TODO: generate from model
        depthFeet = float(depthMeters*3.28084)
        depthFathoms = float(depthMeters*0.546807)
        DBTstring = f'$SDDBT,{round(depthFeet,1)},f,{round(depthMeters,1)},M,{round(depthFathoms,1)},' 
        dbt=checkSum(DBTstring) #.encode('utf-8') 
        #print(dbt)
        serialPort.write(dbt)
    serialPort.close()

else:
    help()  # not the right amount of argument


def help():
    print("Veuillez resayez")

