####################################################################################################>
# Copyright 2019 © Centre Interdisciplinaire de développement en Cartographie des Océans (CIDCO), To>

#@Jacobb13
#https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst TUTORIEL PyUsb

####################################################################################################>
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

reattach = False
#if dev.is_kernel_driver_active(0):
# reattach = True
# dev.detach_kernel_driver(0)
if dev is None:
 raise ValueError('Our device is not connected')
print("Connected")

# set the active configuration
c = 1
for config in dev:
 print('config', c)
 print('Interfaces', config.bNumInterfaces)
 for i in range(config.bNumInterfaces):
  if dev.is_kernel_driver_active(i):
   dev.detach_kernel_driver(i)
  print(i)
 c+=1

dev.set_configuration()


dev.set_configuration()
cfg = dev.get_active_configuration()
interface_number = cfg[(0,0)].bInterfaceNumber
#alternate_setting = usb.control.get_interface(dev, interface_number)
alternate_setting = 0
intf = usb.util.find_descriptor(cfg, bInterfaceNumber=interface_number, bAlternateSetting=alternate_>

ep = usb.util.find_descriptor(
 intf, custom_match=lambda e:
 usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)

#dev.detach_kernel_driver(interface)

ep.write("\r" + "allo" "\n\r")


#necessaire pour eviter l'erreur : "ressource busy"
#usb.util.dispose_ressources(dev)
if reattach:
 dev.attach_kernel_driver(0)

  

