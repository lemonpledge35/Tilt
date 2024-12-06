import numpy as np
import time
import datetime

from beacontools import BeaconScanner, parse_packet, IBeaconFilter
global temp
global sg

def callback(bt_addr, rssi, packet, additional_info):
    global temp
    global sg
    #t = datetime.datetime.now()
    temp_temp = packet.major
    sg_temp = packet.minor
    #print("Temperature: %i, Specific Gravity: %d"% (temp,sg))
    #print("<%s, %d> %u %s" % (bt_addr, rssi, packet, additional_info))
    #print("returning temp, sg")
    temp = temp_temp
    sg = sg_temp/1000

#scanner = BeaconScanner(callback, device_filter=IBeaconFilter(uuid="a495bb50-c5b1-4b44-b512-1370f02d74de"))

def get_values():
    global temp
    global sg
    temp = 0
    sg = -10
    scanner = BeaconScanner(callback, device_filter=IBeaconFilter(uuid="a495bb50-c5b1-4b44-b512-1370f02d74de"))
    scanner.start()
    i = 0
    while sg < 0:
        i += 1
        time.sleep(1)
        if i > 5:
            print('Time out on Tilt read')
            return 0,0
    scanner.stop
    return temp,sg
'''
temp = 0
sg = -10
scanner.start()
while sg < -0:
    pass
scanner.stop()
time = datetime.datetime.now()
print(f'Time: {time}')
print(f'Temperature: {temp}')
print(f'Specific Gravity: {sg}')

'''