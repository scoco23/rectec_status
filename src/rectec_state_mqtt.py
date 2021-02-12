import json
import pytuya
import time
import paho.mqtt.client as mqtt
from os import environ

client = mqtt.Client()

mqttserver = environ['MQTT_ADDR']
mqttport = int(environ['MQTT_PORT'])
mqtttopic = environ['MQTT_TOPIC']
gwid = environ['GRILL_ID']
ip = environ['GRILL_IP']
productkey = environ['PRODUCTKEY']
updatesecs = int(environ['UPDATE_SECS'])

client.connect(mqttserver, mqttport, 60)

while True:
	# Specify the smoker and get its status
	d = pytuya.OutletDevice(gwid, ip, productkey)
	data = d.status()

	# Enable debug to see the raw JSON
	Debug = False
	#Debug = True
	if Debug:
	    raw = json.dumps(data, indent=4)
	    print(raw)

	# Simple if statement to check if the smoker is on
	rt_state = data['dps']['1']

	if rt_state:
	    print('RecTec is on')
	else:
	    print('RecTec is off')

	# The following values are based on observation
	# dps = '102' & '103' might be swapped
	print('Target Temperature: %r' % data['dps']['102'])
	print('Current Temperature: %r' % data['dps']['103'])
	# When smoker is off (data['dps']['1] = False)
	# values of probes might be based on last "on"
	print('Probe A Temperature: %r' % data['dps']['105'])
	print('Probe B Temperature: %r' % data['dps']['106'])
	# Output to MQTT
	client.publish(mqtttopic + "/status", payload=data['dps']['1'], qos=0, retain=False)
	client.publish(mqtttopic + "/ctemp", payload=data['dps']['103'], qos=0, retain=False)
	client.publish(mqtttopic + "/ttemp", payload=data['dps']['102'], qos=0, retain=False)
	client.publish(mqtttopic + "/patemp", payload=data['dps']['105'], qos=0, retain=False)
	client.publish(mqtttopic + "/pbtemp", payload=data['dps']['106'], qos=0, retain=False)
	# sleep
	time.sleep(updatesecs)
