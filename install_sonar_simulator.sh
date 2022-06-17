#!/bin/bash

    echo "<*> disable auto-update"
    sudo systemctl stop unattended-upgrades
    echo "[+] Updating repositories"
    sudo apt update | tee log.txt
    echo "[+] Updating base system"
    sudo apt dist-upgrade -y | tee -a log.txt
    echo "[+] Updating applications"
    sudo apt upgrade -y | tee -a log.txt
    echo "[+] Installing rtl-ais packages..."
    sudo apt install -y build-essential python3-pip| tee -a log.txt
    echo "[+] Cloning sonarSimulator git repository"
    cd /home/ubuntu
    git clone https://github.com/ | tee -a ~/log.txt
    echo "[+] Setting Baud Rate to 4800"
    stty4800
    echo "[+] Initialization complete."    
    echo "[+] To start program : "
    echo "[+] python3 nmeaGENARATOR.py [DEPTH (IN METERS)]"
    
    
