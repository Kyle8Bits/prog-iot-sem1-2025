#!/usr/bin/env python3
# more info: https://pypi.org/project/python-crontab/

#check the crontab available : crontab -l
#stop/start the crontab: sudo /etc/init.d/cron stop/start

from datetime import datetime
from sense_hat import SenseHat

time = datetime.now().strftime("%H:%M")
sense = SenseHat()
sense.show_message('Time is {}'.format(time), scroll_speed=0.1)
