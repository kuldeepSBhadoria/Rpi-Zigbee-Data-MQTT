# Rpi-Zigbee-Data-MQTT

Read IR-9ZBS-SL data from Rpi Reference:-(http://static6.arrow.com/aropdfconversion/2c514557bac4d53fb3bfe80acc2458767af5a56/2895789965914218ug129-zigbee-gateway-ref-design-guide.pdf)

Some commands to form a zignee netwrok:-
(This is auto start app in RPi /opt/siliconlabs/zigbeegateway/bin/siliconlabsgateway -n 0 -p /dev/ttyACM0)
#plugin network-creator start 1
#plugin network-creator-security open-network

Note:-If you have to create new netwrok then use these commands using MQTT Topic gw/<eui64_id>/commands and send to gw/EUI
    # mosquitto_pub -h 192.168.42.1 -t gw/000B57FFFE0BCA7E/commands -m '{"commands":[{"command" :"plugin network-creator-security open-network"}]}'



Subscribe to MQTT topics
mosquitto_sub -h 192.168.42.1 -t gw/000B57FFFE0BCA7E/zclresponse

Whenever motion detected you will get this in subscriber
{"clusterId":"0x0500","commandId":"0x00","commandData":"0x040000010000","clusterSpecific":true,"deviceEndpoint":{"eui64":"0x00124B00168F5E80","endpoint":1}}
{"clusterId":"0x0500","commandId":"0x00","commandData":"0x050000010000","clusterSpecific":true,"deviceEndpoint":{"eui64":"0x00124B00168F5E80","endpoint":1}}

commandData : 05 means motion detected
