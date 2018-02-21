# rm3_ifttt - Broadlink RM3 to IFTTT connector
This simple Python script enables you to connect your Broadlink RM3 mini to [IFTTT](https://ifttt.com/) in order to automate your IoT use cases.

## Credits
Credit goes to https://github.com/TheGU/rm3_mini_controller (which itself is based on https://github.com/davorf/BlackBeanControl and https://github.com/mjg59/python-broadlink).

This repository only exposes these APIs using the **web.py** framework.

## Setup
Clone this repository on your local machine and install dependencies:
```
git clone https://github.com/arthur073/rm3_ifttt
cd rm3_ifttt
pip install -r rm3_mini_controller/requirements.txt
```
Discover the broadlink device on your network:
```
python rm3_mini_controller/test_run.py
```
This above script will scan your network for any Broadlink device and print its IP address, port and MAC address. Once found, update the file `rm3_mini_controller/BlackBeanControl.ini` with this information, so that it looks like this:
```
[General]
IPAddress = 192.168.1.1
Port = 80
MACAddress = AA:BB:CC:DD:EE:FF
Timeout = 10
``` 
Open the `run.py` file and update the `passcode` variable to the value you want (this will later be used in IFTTT):
```python
# User variables
passcode="mygreatpassword"
```
To start the web server, run: 
```
python run.py 1234
```
where `1234` is the port number on which the web server will be launched.

You are all set!

## Usage
### Generic principle
Once started, the web server will listen for any incoming POST requests on the specified port. The 
request needs to specify the **action** you want to perform and the **secret password**. 
- The first time the request is launched, the device is in **learning** mode (white LED)
- Once the action is learned, the device is in **play** mode and will repeat the learned infrared code

### Example with Curl
Use the following command to send a post request to your web server: 
```
curl -X POST http://localhost:1234 -H 'content-type: application/json' -d '{"auth":"mygreatpassword", "action":"action_1"}
``` 
where `mygreatpassword` is your secret password and `action_1` the name of the action you want to perform on your Broadlink device. 

### IFTTT
With IFTTT, you need to use the [Maker channel](https://ifttt.com/maker_webhooks) in order to send POST requests to your web server. The following parameters need to be specified: 
Parameter|Value
---------|-----
URL|URL of your webserver. You need to specify the external IP which you can get by running `curl ifconfig.co`
Method|POST
Content type|application/json
Body|`{"auth":"mygreatpassword","action":"action_1"}` where `mygreatpassword` and `action_1` need to be changed as explained in `curl` example


