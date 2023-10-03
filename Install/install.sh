sudo apt install python3 python-is-python3 python3-pip -y

sudo bash -c 'cat << EOF3 > /etc/systemd/system/nmea.service
[Unit]
Description=Launch NMEA Simulator on boot.

[Service]
Type=simple
ExecStart=/home/ubuntu/SonarSimulator/Script/autolaunch.sh

[Install]
WantedBy=multi-user.target
EOF3'

sudo chmod 755 /etc/systemd/system/nmea.service
sudo systemctl enable nmea
sudo systemctl start nmea
sudo systemctl status nmea

