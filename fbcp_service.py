#!/usr/bin/python
from time import sleep
import os
try:
    while True:
        print "fbcp launched!"
	os.system("./home/pi/rpi-fbcp/build/fbcp")
        sleep(60)
except KeyboardInterrupt, e:
    logging.info("Stopping...")
