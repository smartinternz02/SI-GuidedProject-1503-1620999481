import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json
import random as r

#Provide your IBM Watson Device Credentials
organization = "178vg8"
deviceType = "IOTdevice"
deviceId = "1001"
authMethod = "token"
authToken = "1234567890"


# Initialize the device client.
W=0
L=0

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        W=r.randint(0,50)
        L=r.randint(0,100)
        #Send Temperature & Humidity to IBM Watson
        data = {"d":{ 'waterLevel' : W, 'lightIntensity': L }}
        print (data)
        def myOnPublishCallback():
            print ("Published Water level = %s  %% " % W, "Light Intensity= %s  Cd" % L, "to IBM Watson")

        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
       # deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
