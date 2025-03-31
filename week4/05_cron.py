#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='kylemai')
cron.remove_all()

#add new cron job
job  = cron.new(command='/home/kylemai/Documents/Pi/week4/Sensors_Database/04_timesense.py')

#job settings
job.minute.every(1)
cron.write()
