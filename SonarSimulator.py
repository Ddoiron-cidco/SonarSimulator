############################################################################################################
# Copyright 2019 © Centre Interdisciplinaire de développement en Cartographie des Océans (CIDCO), Tous droits réservés

#@Jacobb13
#https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst TUTORIEL PyUsb

############################################################################################################
#Setup : 
#sudo install pip3
#sudo pip3 install pyusb

####################
##Questions  : 
# Transfer type ? interrupt ? 


######
import os
import sys
import usb.core
import usb.util

## MACHINE
 ##IdVendor: 0x0403 
 ##IdProduct: 0x6001
 
## Rpi
VID=0x067b
PID=0x2303
## "lsusb -v" sur le rpi pour connaitre les infos

#bEndpointAddress : 0x02 (EP 2 OUT)


dev = usb.core.find(idVendor=VID, idProduct=PID)
if dev is None:
 raise ValueError('Our device is not connected')

print("ISsa connected")
# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

dev.write("TEST")
print("TERMINATE")


