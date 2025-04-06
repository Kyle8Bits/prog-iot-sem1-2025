#!/usr/bin/env python3
import bluetooth
import time
from sense_hat import SenseHat

# Main function
def main():
    user_name = input("Enter your name: ")
    device_mac = input("Enter the MAC address of your phone (as seen with bluetoothctl): ")
    search(user_name, device_mac)

# Search for device based on MAC address
def search(user_name, target_mac):
    sense = SenseHat()

    while True:
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        time.sleep(3)

        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=False)
        
        if target_mac.upper() in [mac.upper() for mac in nearby_devices]:
            print("Hi {}! Your phone is nearby. MAC: {}".format(user_name, target_mac))
            temp = round(sense.get_temperature(), 1)
            sense.show_message(f"Hi {user_name}! Temp: {temp}°C", scroll_speed=0.1)
        else:
            print("Could not find target device nearby...")

# Execute program
main()
