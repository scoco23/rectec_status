# rectec_mqtt

VERY ALPHA!

Forked from https://github.com/SDNick484/rectec_status/  His intro below

*Scripts to talk to [Rec Tec Grills pellet smokers](http://www.rectecgrills.com/) with the Rec Tec Wi-Pellet WiFi controllers.  Supported models include the  RT-340, RT-590, & RT-700 which all include the WiFi controller by default, and the RT-300 & RT-680 that are upgradable to the WiFi controller.*

*The WiFi controllers on Rec Tec smokers leverage the [Tuya Smart IoT platform](https://en.tuya.com/) which can be reached over TCP or MQTT.  The scripts currently leverage [python-tuya](https://github.com/clach04/python-tuya) and communicate via TCP on port 6668 over the LAN.  Through additional exploration and collaboration, I'd like to expand the scripts to support remote access via MQTT.*

I'm using tinytuya instead of pytuya, as it seems pytuya isn't being maintained anymore.

## Usage:

Must be ran on the host network in order to discover the RecTec.

docker run --network host --env MQTT_ADDR=your.mqttserver.local scoco23/rectec


Some ENVs:

The address of your MQTT server:
ENV MQTT_ADDR="192.168.254.1"

Its port:
ENV MQTT_PORT="1883"

The topic:
ENV MQTT_TOPIC="sensor/rectec"

How often to poll and update, in seconds:
ENV UPDATE_SECS="30"

