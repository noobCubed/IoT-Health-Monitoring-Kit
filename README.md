# IoT Health Monitoring Kit

A portable kit for easy measurement of certain health parameters like Blood Pressure, Temperature and ECG. Can be deployed in homes to avoid unnecessary trips to hospitals and costs involved. The kit is made using a Raspberry Pi 3B and a 7 inch Resistive Touch Screen, along with the sensor modules for each parameter involved. The Graphical User Interface for the kit was made using the Kivy Library.

## Getting Started

Instructions for setting up the Kivy library on the Raspberry Pi

### Prerequisites

Perform the following steps on the Raspberry Pi command terminal to set up the Kivy library

1. Updating the software

```
sudo apt-get update
sudo apt-get upgrade
```

2. Reboot the Pi

```
sudo reboot
```

3. Installing the dependencies

```
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev libmtdev-dev xclip xsel
```

4. Install Cython

```
sudo pip install -U Cython
```

5. Install Kivy using pip3

```
sudo pip3 install git+https://github.com/kivy/kivy.git@master
```

6. Run an example for the config.ini file to be created

```
cd /usr/local/share/kivy-examples/demo/showcase
python main.py
```

7. To configure Kivy to use touch as an input source

```
cd /usr/local/lib/python2.7/dist-packages/kivy
sudo nano ~/.kivy/config.ini
```

Goto the *[input]* section and add the following

```
mouse = mouse
mtdev_%(name)s = probesysfs,provider=mtdev
hid_%(name)s = probesysfs,provider-hidinput
```

Goto the *[modules]* section and add the following to enable the mouse cursor as the Kivy window will work fullscreen on top of the mouse cursor by default

```
touchring = show_cursor=true
```

This will enable a ring to point out the cursor for you 

8. Try the example again with touch
