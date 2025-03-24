import json
import time
from sense_hat import SenseHat
from pixels import number_pixels
import sqlite3

# Define colors
blue = (0, 0, 255)
red = (255,0,0)
green = (0,255,0)
purple = (128,0,128)
yellow = (255,220,0)
white = (255,255,255) # White
black = (0, 0, 0)   # Black (background)

#init sense
sense = SenseHat()


class Config:
    def __init__(self, config_file):
        self.config = self.read_json_file(config_file)
        print("created config object")
    
    def read_json_file(self, file):
        with open(file, "r") as f:
            data = json.load(f)
        return data
    
    def get_category(self, temperature, humidity):
        comfort_temp = self.config["comfortable_temperature_range"].split("-")
        comfort_humid = self.config["comfortable_humidity_range"].split("-")
     
        lower_comfort_temp = int(comfort_temp[0])
        upper_comfort_temp = int(comfort_temp[1])
        lower_comfort_humid = int(comfort_humid[0])
        upper_comfort_humid = int(comfort_humid[1])

        cold_temp = int(self.config["cold_temperature_upper_limit"])
        hot_temp = int(self.config["hot_temperature_lower_limit"])
        dry_humid = int(self.config["dry_humidity_upper_limit"])
        wet_humid = int(self.config["wet_humidity_lower_limit"])

        category = ["",""]
        if(temperature < cold_temp):
            category[0] = "Cold"
        elif(temperature > hot_temp):    
            category[0] = "Hot"
        elif(temperature >= lower_comfort_temp and temperature <= upper_comfort_temp):
            category[0] = "Comfortable"

        if(humidity < dry_humid):
            category[1] = "Dry"
        elif(humidity > wet_humid):
            category[1] = "Wet"
        elif(humidity >= lower_comfort_humid and humidity <= upper_comfort_humid):
            category[1] = "Comfortable"

        return category

class SensorData:
    def __init__ (self, temperature, humidity, config_data):
        self.temperature = temperature
        self.humidity = humidity
        self.config_data = config_data
        print("created sensor object")

    def category(self):
        return self.config_data.get_category(self.temperature, self.humidity)

    def show_number(self ,num1, num2, matrix, color):
        for x, y in number_pixels[num1]:
            index = (y+3) * 8 + x
            matrix[index] = color
        
        for a,b in number_pixels[num2]:
            index = (b+3) * 8 + (a + 5)
            matrix[index] = color
        sense.set_pixels(matrix)

    def show_text(self ,text, matrix):
        if text == "temp":
            for x, y in number_pixels[10]:
                index = y * 8 + (x+2)
                matrix[index] = white
        elif text == "humid":
            for a, b in number_pixels[11]:
                index = b * 8 + (a+2)
                matrix[index] = white
        sense.set_pixels(matrix)

    def show_result(self):
        temp_str = str(self.temperature)
        humid_str = str(self.humidity)

        f_temp_num = int(temp_str[0])
        s_temp_num = int(temp_str[1])

        f_humid_num = int(humid_str[0])
        s_humid_num = int(humid_str[1])
        
        category = self.config_data.get_category(self.temperature, self.humidity)

        if category[0] == "Cold":
            temp_color = blue
        elif category[0] == "Hot":
            temp_color = red
        else:
            temp_color = green
        
        if category[1] == "Dry":
            humid_color = yellow
        elif category[1] == "Wet":
            humid_color = purple
        else:
            humid_color = green

        matrix = []

        matrix = [black] * 64 
        self.show_text("temp", matrix)
        self.show_number(f_temp_num, s_temp_num, matrix, temp_color)
        time.sleep(5)
        sense.clear()

        time.sleep(1)
        matrix = [black] * 64 

        self.show_text("humid",matrix)
        self.show_number(f_humid_num, s_humid_num,matrix, humid_color)
        time.sleep(5)
        sense.clear()

        time.sleep(1)

    def save_data(self):
        conn = sqlite3.connect('climate.db')
        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        # Create a table
        cursor.execute('''CREATE TABLE IF NOT EXISTS temperature (id INTEGER PRIMARY KEY, value INTEGER, zone INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS humidity (id INTEGER PRIMARY KEY, value INTEGER, zone INTEGER)''')

        cursor.execute("INSERT INTO temperature (value, zone) VALUES (?, ?)", (self.temperature, self.category()[0]))
        cursor.execute("INSERT INTO humidity (value, zone) VALUES (?, ?)", (self.humidity, self.category()[1]))

        # Commit the changes
        conn.commit()

def main():

    config = Config("config.json")
    sensor = SensorData(0, 0, config)

    while True:
        temperature = int(sense.get_temperature())
        humidity = int(sense.get_humidity()) 

        sensor.temperature = int(temperature)  # Get the latest temperature
        sensor.humidity = int(humidity)  # 
    
        print(temperature)
        print(humidity)

        sensor.save_data()
        sensor.show_result()

if __name__ == "__main__":
    main()
