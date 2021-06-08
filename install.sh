#!/bin/bash
if [[ "$EUID" = 0 ]]; then
    echo "Already root"
else
    sudo -k
    if sudo true; then
        echo "Sucessfully got root"
    else
        echo "Wrong password"
        exit 1
    fi
fi

sudo pip install pyautogui

sudo mkdir /etc/RPiSwitchJoystick
sudo cp config.txt /etc/RPiSwitchJoystick/
sudo cp service.py /etc/RPiSwitchJoystick/
sudo cp RPiSwitchJoystick.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/RPiSwitchJoystick.service
sudo chmod +x /etc/RPiSwitchJoystick/service.py

sudo systemctl daemon-reload
sudo systemctl enable RPiSwitchJoystick.service
sudo systemctl start RPiSwitchJoystick.service

echo "Done"