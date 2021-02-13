# rectec_mqtt

Forked from https://github.com/SDNick484/rectec_status/  His intro below

*Scripts to talk to [Rec Tec Grills pellet smokers](http://www.rectecgrills.com/) with the Rec Tec Wi-Pellet WiFi controllers.  Supported models include the  RT-340, RT-590, & RT-700 which all include the WiFi controller by default, and the RT-300 & RT-680 that are upgradable to the WiFi controller.*

*The WiFi controllers on Rec Tec smokers leverage the [Tuya Smart IoT platform](https://en.tuya.com/) which can be reached over TCP or MQTT.  The scripts currently leverage [python-tuya](https://github.com/clach04/python-tuya) and communicate via TCP on port 6668 over the LAN.  Through additional exploration and collaboration, I'd like to expand the scripts to support remote access via MQTT.*

## Usage:

This fork takes the RecTec info and sends it to an MQTT server.

The container currently DOES NOT implement SDNick484's discovery script, so you'll need to start there to determine some info from your grill.  With that info, set these ENVs:

The address of your MQTT server:
ENV MQTT_ADDR="192.168.254.1"

Its port:
ENV MQTT_PORT="1883"

The topic:
ENV MQTT_TOPIC="sensor/rectec"

Your grill ID (from the discovery script):
ENV GRILL_ID="SomeString"

Your grill IP (also from the discovery script):
ENV GRILL_IP="192.168.254.123"

Your Grill product key (also from the discovery script):

How often to poll and update, in seconds:
ENV UPDATE_SECS="30"