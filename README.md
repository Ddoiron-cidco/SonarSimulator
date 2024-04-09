# README for nmeaSIMULATOR.py
## Sonar simulator NMEA-0183



### foncitonnalities :

Generate nmea-0183 string of types  :  
- Depth of water (SDDPT)

### HOW TO MAKE IT WORK: 
    
On a Raspberry pi : 

1. Install ubuntu server on as sdcard with the user ubuntu

2. Connect the usb serial adapter on the Raspberry

3. apply the power on the raspberry

4. validate if the serial adapter is detected by the OS
    ls /dev/ttyU*
	  you should see ttyUSB0
   
5. clone the repository in /home/ubuntu

6. Validate and modify the setting for the serial port and baudrate in the autolaunch.sh
    nano /home/ubuntu/SonarSimulator/autolaunch.sh
	  python /home/ubuntu/SonarSimulator/Script/sonar_simulator_DPT.py /dev/ttyUSB0 9600
	  the 2 last argument are the serial port and the baudrate
	  ex:
	  python /home/ubuntu/SonarSimulator/Script/sonar_simulator_DPT.py /dev/ttyUSB1 9600
	  python /home/ubuntu/SonarSimulator/Script/sonar_simulator_DPT.py /dev/ttyAMA0 115200

7. go in the install directory and run the installation script
    cd /home/ubuntu/SonarSimulator/Install
    ./install.sh

The script is installed as a service. 
If you do some modification in the autolaunch.sh file you have to relaunch the service. 
sudo systemctl restart nmea

to show the status of the service : sudo systemctl status nmea
to start the service : sudo systemctl start nmea
to stop the service : sudo systemctl stop nmea



