# set base image (host OS)
#FROM python:3.8
#FROM python:3.6.6-alpine3.6
FROM python:alpine

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

ENV MQTT_ADDR="192.168.254.1"
ENV MQTT_PORT="1883"
ENV MQTT_TOPIC="sensor/rectec"
ENV GRILL_ID="X"
ENV GRILL_IP="192.168.254.123"
ENV PRODUCTKEY="1CwNbNLE8r70WR7t"
ENV UPDATE_SECS="30"


# install dependencies
#RUN apk update && apk add libressl-dev postgresql-dev libffi-dev gcc musl-dev python3-dev 
RUN pip install -r requirements.txt
RUN pip install pytuya
# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./rectec_state_mqtt.py" ] 
