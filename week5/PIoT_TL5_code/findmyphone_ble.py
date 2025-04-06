#!/usr/bin/env python3
import asyncio
import time
from sense_hat import SenseHat
from bleak import BleakScanner

# Main function
def main():
    user_name = input("Enter your name: ")
    device_name = input("Enter the name of your phone (as seen in BLE): ")
    
    try:
        asyncio.run(search(user_name, device_name))
    except KeyboardInterrupt:
        print("\nExited by user.")

# BLE Search function
async def search(user_name, device_name):
    sense = SenseHat()
    print(f"Searching for {device_name}... Press Ctrl+C to stop.\n")

    while True:
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print(f"Currently: {dt}")
        
        devices = await BleakScanner.discover(timeout=5.0)

        found = False
        for d in devices:
            if d.name == device_name:
                print(f"Hi {user_name}! Your phone ({device_name}) is nearby. MAC: {d.address}")
                temp = round(sense.get_temperature(), 1)
                sense.show_message(f"Hi {user_name}! Temp: {temp}°C", scroll_speed=0.05)
                found = True
                break

        if not found:
            print("Could not find target device nearby...")

        time.sleep(3)

# Execute program
main()
