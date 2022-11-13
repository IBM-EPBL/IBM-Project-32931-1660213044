import time
import sys
import ibmiotf.application
import ibmiotf.device 
import random


organization = "u0b4fr" 
deviceType = "TestdriveDevice" 
deviceId = "TestdriveDevice_1" 
authMethod = "token" 
authToken = "8300113450"

try:
       deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
       deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
       print("Caught exception connecting device: %s" % str(e))sys.exit()
       deviceCli.connect()
while True:

          temp=random.randint(0,100)
          Humid=random.randint(0,100)
          Gas=random.randint(0,100)
           data = { 'temp' : temp, 'Humid': Humid,’Gas’:gas }
           #print data
def myOnPublishCallback():
         print ("Published Temperature = %s C" % temp, "Humidity = %s %%" %Humid, “Gas Concentration = %s”%Gas"to IBM Watson")
         success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
if notsuccess:
        print("Not connected to IoTF")
time.sleep(10)
deviceCli.commandCallback = myCommandCallback
deviceCli.disconnect()
