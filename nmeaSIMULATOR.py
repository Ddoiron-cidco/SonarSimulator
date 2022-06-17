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


outputTypeList = ['GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA'] 
outputType=[]

def run(arg_outputTimer, outputType):
#def run():
    sim = Simulator()
    f = open("/dev/ttyUSB0", "w")
    outputTimer =int(arg_outputTimer)
    #print("ici", arg_outputType)
    #outputType = []
    #outputType.append(arg_outputType)
    with sim.lock:
        # Can re-order or drop some
        sim.gps.output = tuple(outputType)
        #sim.gps.output = ('GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA')
        sim.gps.num_sats = 14
        sim.gps.lat = 1
        sim.gps.lon = 3
        sim.gps.altitude = -13
        sim.gps.geoid_sep = -45.3
        sim.gps.mag_var = -1.1
        sim.gps.kph = 60.0
        sim.gps.heading = 90.0
        sim.gps.mag_heading = 90.1
        sim.gps.date_time = datetime.now(TZ_LOCAL)  # PC current time, local time zone
        sim.gps.hdop = 3.1
        sim.gps.vdop = 5.0
        sim.gps.pdop = (sim.gps.hdop ** 2 + sim.gps.vdop ** 2) ** 0.5
        # Precision decimal points for various measurements
        sim.gps.horizontal_dp = 4
        sim.gps.vertical_dp = 1
        sim.gps.speed_dp = 1
        sim.gps.time_dp = 2
        sim.gps.angle_dp = 1
        # Keep straight course for simulator - don't randomly change the heading
        sim.heading_variation = 0
    sim.generate(outputTimer, output=f)
   


def loar_arg():
    # Detect and load the arguments
    len_arg=len(sys.argv)
    if sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-help":
        help()
    else:
        arg_outputTimer = sys.argv[1]
        for args in range(2,len_arg):
            if sys.argv[args] in outputTypeList:
                outputType.append(sys.argv[args])
            elif (sys.argv[args] not in outputTypeList):
                help()
        run(arg_outputTimer, outputType)
        
def help():
    # Display Help
    #os.system('cls')  # clear screen for windows
    os.system('clear')  # clear screen for linux and mac
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Help")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("HOW TO RUN THE PROGRAM:")
    print("Syntax: python3 nmeaSIMULATOR [OPTION1][OPTION2]")
    print("example: python3 nmeaSIMULATOR 100 GGA ")
    print("")
    print("Options:")
    print("")
    print("-help or -h                           Print Help Page")
    print("[OPTION1] = [Time in seconds]         Duration of the nmea generator in seconds ")
    print("[OPTION2] = [output type]             Can be multiple choices, choose in this list :")
    print(" 'GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA'")
    print("")
    print("Another example : python3 nmeaSIMULATOR 10 GGA VTG")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("IF NOT WORKING : ")
    print("Check the baudrate of both devices : ")
    print("for NEMA-0183, it should be configured at 4800")
    print("To verify baudrate : stty")
    print("To set baudrate : stty 4800")
    print("BE SURE TO BE LAUNCHING THE PROGRAM ON THE Raspberry pi !")
    


if len(sys.argv) >= 3:
    loar_arg()
    # except KeyboardInterrupt:
    #     print("Caught keyboard interrupt, exiting")
    # except ConnectionResetError:
    #     print("Connection interrupt, exiting")
else:
    help()  # not the right amount of argument


