from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Read pressure with the Sense HAT
pressure = sense.get_pressure()
print(pressure)

# Temperature
sense.clear()
temp = sense.get_temperature()
print(temp)

# Humidity
sense.clear()
humidity = sense.get_humidity()
print(humidity)