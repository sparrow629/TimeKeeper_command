# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: timer on all the os which is created as a new thread
  Created: 2017-8-31
"""
import threading
import time
import sys
import datetime
import os
from threading import *

 
class TimeKeeper(Thread):
	def run(self):
		print "Start timing!"
		start_time, start_datetime = time.time(), datetime.datetime.now()
		self.ifdo = True
		while self.ifdo:
			stop, stopd = time.time(), datetime.datetime.now()
			spend, time_dis = (stop - start_time), (stopd - start_datetime)
			sys.stdout.write('\r' + '%s' % time_dis)
			sys.stdout.flush()
		Time_keeper = round(spend,2)
		print "\nEnd timing!\n\nSpend: %s s " % Time_keeper
 
	def stop(self):
		self.ifdo = False;
 
def time_keeper():
	raw_input()
	timing = TimeKeeper()
	timing.setDaemon(True)
	timing.start()
	if raw_input() != 'q':
		timing.stop()
		timing.join()
	else:
		print "\nYou have input 'q' button to interrupt timing!\n"
		os._exit(0)

if __name__ == '__main__':
    key = None
    while key != 'q':
        print "Strike the <Enter> button will start timing:"
        time_keeper()
        print "\nInput q to quit, or restart!"
        key = raw_input()





