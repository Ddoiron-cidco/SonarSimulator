# README for nmeaSIMULATOR.py
## Sonar simulator NMEA-0183

*implementation of PyPi : nmeasim https://pypi.org/project/nmeasim/#description*

### foncitonnalities :

Generate nmea-0183 string of types  :  
- Geospatial (GGA, GLL, RMC, VTG, ZDA) - simulated using a consistent location/velocity model, time using machine time (not NTP, unless the machine happens to be NTP synchronised).  
- Satellites (GSA, GSV) - faked with random azimuth/elevation.


### HOW TO MAKE IT WORK: 

On a linux machine : cat /dev/ttyUSB0    
On rpi : python3 nmeaSIMULATOR.py 10 GGA    


### install requirements for nmeaSim
install_requires =

    pyserial

    geographiclib

    importlib.metadata; python_version<'3.8'

