import time
import sqlite3
from sense_hat import SenseHat

dbname = "sensehat.db"
sample_freq = 1 # time in seconds

# get data from SenseHat sensor
def get_sensehat_data():	
    sense = SenseHat()
    temp = sense.get_temperature()
	
    if temp is not None:
        temp = round(temp, 1)
        log_data(temp)

# log sensor data on database
def log_data(temp):	
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?))", (temp,))
    conn.commit()
    conn.close()

# display database data
def display_data():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SenseHat_data"):
        print(row)
    conn.close()

# main function
def main():
    for i in range (0, 3):
        get_sensehat_data()
        time.sleep(sample_freq)
    display_data()

# Execute program 
main()
