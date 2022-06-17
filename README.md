# SonarSimulator
Simulateur de sonar NMEA 0183

Pour faire fonctionner : 

sur machine linux : cat /dev/ttyUSB0 ## pour écouter le port usb  
sur rpi  : python3 nmeaSIMULATOR.py 10 GGA  
sinon python3 nmeaSIMULATOR.py -h ## pour afficher help section  


### install requirements for nmea sim
install_requires =

    pyserial

    geographiclib

    importlib.metadata; python_version<'3.8'

