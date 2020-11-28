# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import paho.mqtt.client as mqtt
import time
broker='192.168.42.1'


# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=kd-kd-kd.azure-devices.net;DeviceId=my-motion;SharedAccessKey=FP3xU42MPWBg87oLEAayklXpm0uWMRWwvgpdEtoJndk="

# Define the JSON message to send to IoT Hub.

MSG_TXT = '{{"motion": {detected}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_send():
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        # Send the message.
        print( "Sending message: {}".format(MSG_TXT) )
        client.send_message(MSG_TXT)
        print ( "Message successfully sent" )
        client.disconnect()

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print("on_Message")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    iothub_client_telemetry_send()

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    print ( "IoT Hub send data" )
    print ( "Press Ctrl-C to exit" )

    #iothub_client_telemetry_send()

    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    # mqttc.on_log = on_log
    mqttc.connect(broker, 1883, 60)
    mqttc.subscribe("gw/000B57FFFE0BCA7E/zclresponse", 0)

    mqttc.loop_forever()