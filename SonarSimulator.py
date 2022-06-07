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
 ##IdVendor: 0x067b
 ##idProduct: 0x2303
## "lsusb -v" sur le rpi pour connaitre les infos

#bEndpointAddress : 0x02 (EP 2 OUT)


dev = usb.core.find(idVendor=0x0403, idProduct=0x6001)
if dev is None:
 raise ValueError('Our device is not connected')
help(usb.util)

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
 intf,
 # match the first OUT endpoint
 custom_match = \
 lambda e: \
 usb.util.endpoint_direction(e.bEndpointAddress) == \
 usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')    
    
    
    
    
       
#f = open("output.txt","w+")
#for i in 10 :
# f.append(i)
# i+=1
 
