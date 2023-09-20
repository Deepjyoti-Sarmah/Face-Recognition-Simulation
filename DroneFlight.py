import collections.abc
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# connect to the vehicle
import argparse
parse = argparse.ArgumentParser(description='commands')
parse.add_argument('--connect')
args = parse.parse_args()

connection_string = args.connect

print('Connection to the vehicle on %s'%connection_string)
vehicle = connect(connection_string, wait_ready=True)

# Define the function for takeoff
def arm_and_takeoff(tgt_altitude):
    print("Arming motos")

    while not vehicle.is_armable:
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    print("TakeOff")
    vehicle.simple_takeoff(tgt_altitude)

    # wait to reach the target altitude
    while True:
        altitude = vehicle.location.global_relative_frame.alt

        if altitude >= tgt_altitude -1:
            print("Altitude reached")
            break

        time.sleep(1)


# Main Program 
arm_and_takeoff(10)

# set the default speed
vehicle.airspeed = 7

# Go to wait points
print("go to wpl")
wpl = LocationGlobalRelative(35.9872609, -95.8753037, 10)

vehicle.simple_goto(wpl)

# Write the face recognition code here
time.sleep(30)

# Comming back
print("comming back")
vehicle.mode = VehicleMode("RTL")

time.sleep(20)

# close connection
vehicle.close()

# sudo python dronekit_test.py --connect udp:127.0.0.1:14551
# dronekit-sitl copter-3.3 --home=24.6850, 92.7512,584,353