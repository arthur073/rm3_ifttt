# rm3_ifttt - Broadlink RM3 to IFTTT connector
This simple Python script enables you to connect your Broadlink RM3 mini to [IFTTT](https://ifttt.com/) in order to automate your IoT use cases.

## Credits
Credit goes to https://github.com/TheGU/rm3_mini_controller (which itself is based on https://github.com/davorf/BlackBeanControl and https://github.com/mjg59/python-broadlink).

This repository only exposes these APIs using the **web.py** framework.

## Setup
Clone this repository on your local machine and install dependencies.
```
git clone https://github.com/arthur073/rm3_ifttt
cd rm3_ifttt
pip install -r rm3_mini_controller/requirements.txt
```
Discover the broadlink device on your network.
```
python rm3_mini_controller/test_run.py
```
This above script will scan your network for any Broadlink device and print its IP address, port and MAC address. Once found, update the file `rm3_mini_controller/BlackBeanControl.ini` with this information, so that it looks like this:
```
[General]
IPAAddres s= 192.168.1.1
Port = 80
MACAddress = AA:BB:CC:DD:EE:FF
Timeout = 10
``` 
