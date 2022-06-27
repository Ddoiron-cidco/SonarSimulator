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
        sum^=ord(ch)
    return f'{data}*{sum:02X}\r\n'

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
    while True :      
        while True :
            #Generate GPS
            simulator.generate(DURATION, serialPort)
            #Generate DBT
            depthMeters = 42.0 #TODO: generate from model
            depthFeet = float(depthMeters*3.28084)
            depthFathoms = float(depthMeters*0.546807)
            DBTstring = f'$SDDBT,{round(depthFeet,1)},f,{round(depthMeters,1)},M,{round(depthFathoms,1)},' 
            dbt=checkSum(DBTstring) #.encode('utf-8') 
            serialPort.write(dbt)
        serialPort.close()

else:
    help()  # not the right amount of argument



