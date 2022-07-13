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

def checkSum(data):
    sum=0
    for ch in data:
        if ch != '$':
            sum^=ord(ch)
    return f'{data}*{sum:02X}'

def help():
    # Display Help
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Help")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("HOW TO RUN THE PROGRAM:")
    print("Syntax: python3 p")
    print("Options:")
    print("")
    print("-help or -h                           Print Help Page")
    print(" 'GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA'")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("IF NOT WORKING : ")
    print("Check the baudrate of both devices : ")
    print("for NEMA-0183, it should be configured at 4800")
    print("To verify baudrate : stty -F /dev/ttyUSB0")
    print("To set baudrate : stty -F /dev/ttyUSB0 4800")
    print("BE SURE TO BE LAUNCHING THE PROGRAM ON THE Raspberry pi !")

##################### Main ######################
if len(sys.argv) > 1:
    # Open simulator and output file
    simulator = Simulator()
    serialPort = open("/dev/ttyUSB0", "w")
    #Generate GGA
    # Can re-order or drop some
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
    while True :
        #Generate GPS
        simulator.generate(DURATION, serialPort)
        #Generate DPT
        depthMeters = -1 - simulator.gps.lat - simulator.gps.lon
        depthOffset = 1
        maxDepthRange = 100
        #depthFeet = float(depthMeters*3.28084)
        #depthFathoms = float(depthMeters*0.546807)
        DPTstring = f'$SDDPT,{round(depthMeters,1)},M,{round(depthOffset,1)},{maxDepthRange}' 
        dpt=checkSum(DPTstring) #.encode('utf-8') 
        serialPort.write(f'{dpt}\r\n')
    serialPort.close()

else:
    help()  # not the right amount of argument



