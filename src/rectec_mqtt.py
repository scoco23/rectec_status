import tinytuya
import json
import paho.mqtt.client as mqtt
from time import sleep
import os
from os import environ
from sys import exit


mqttserver = environ['MQTT_ADDR']
mqttport = int(environ['MQTT_PORT'])
mqtttopic = environ['MQTT_TOPIC']
updatesecs = int(environ['UPDATE_SECS'])

# mqttserver = "192.168.254.35"
# mqttport = 1883
# mqtttopic = "sensor/rectec"
# updatesecs = 5


print("Scanning for devices...")
devices = tinytuya.deviceScan()

print("Found %s devices." % len(devices))

global ip
if len(devices) > 0:
	print("Found %s devices. Using the first device found." % len(devices))
	ip = list(devices.keys())[0]
	print("IP: %s\n gwId: %s\n productKey: %s" % (ip, devices[ip]['gwId'], devices[ip]['productKey']))
else:
	exit(os.EX_SOFTWARE)
	
print ("Using %s for the MQTT server IP" % mqttserver)

client = mqtt.Client()
client.connect(mqttserver, mqttport, 60)

d = tinytuya.OutletDevice(devices[ip]['gwId'], ip, devices[ip]['productKey'])

while True:
	data = d.status()

	# Simple if statement to check if the smoker is on
	rt_state = data['dps']['1']

	if rt_state:
	    print('RecTec is on')
	else:
	    print('RecTec is off')


	print('Target Temperature: %r' % data['dps']['102'])
	print('Current Temperature: %r' % data['dps']['103'])
	# When smoker is off (data['dps']['1] = False)
	# values of probes might be based on last "on"
	print('Probe A Temperature: %r' % data['dps']['105'])
	print('Probe B Temperature: %r' % data['dps']['106'])

	# Build and send JSON
	payload = json.dumps({'status':rt_state,'TargeTemp':data['dps']['102'],'CurrentTemp':data['dps']['103'],'ProbeATemp':data['dps']['105'],'ProbeBTemp':data['dps']['106']})
	client.publish(mqtttopic, payload=payload, qos=0, retain=False)
	
	sleep(updatesecs)
