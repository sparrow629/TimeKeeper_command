# -*- coding: utf-8 -*-
"""
  Author:  Sparrow
  Purpose: time routine api for trigger a event
  Created: 2017-9-5
"""
import datetime
import calendar
import sys
import re

AtomTime = '2016-6-6 24:60:60'
Str_format = 'Set time like format as “2017-9-9 24:60:60” :'
Str_Invalid = 'Contain invalid time'
Str_illegal = 'Illegal time format! Using default time in source code:'

class TimingRoutine():
	"""docstring for TimingRoutine"""
	def __init__(self):
		self.Trigger = False
		self.time_valid = True
		print(Str_format)

	def timestring_check(self, settled_time):
		self.stime = settled_time
		
		timereg = r'(\d*)-(\d*)-(\d*) (\d*):(\d*):(\d*)'
		timere = re.compile(timereg)
		time_list = re.findall(timere, self.stime)

		if time_list:
			times = time_list[0]
			try:
				year = int(times[0])
				if year < 1900 or year > 2117:
					year = -1
				month = int(times[1])
				if month < 1 or month > 12:
					year = -1
				else:
					dayRange = calendar.monthrange(year, month)[1]
				day = int(times[2])
				if day < 1 or day > dayRange:
					year = -1
				hour = int(times[3])
				if hour < 0 or hour > 24:
					year = -1
				minute = int(times[4])
				if minute < 0 or minute > 60:
					year = -1
				second = int(times[5])
				if second < 0 or second > 60:
					year = -1
				set_time = (year, month, day, hour, minute, second)
			except:
				print(Str_Invalid)
				set_time = AtomTime

		else:
			print(Str_illegal)
			set_time = AtomTime
		
		return set_time

	def get_now(self):
		self.now = datetime.datetime.now()
		time_now = self.now.strftime('%Y-%m-%d %H:%M:%S')
		# print(time_now)
		return time_now

	def timing_routine(self, time_set_str):
		print("Set time: %s\n" % time_set_str)
		while not self.Trigger and self.time_valid:
			time_now_str = self.get_now()
			time_set = self.timestring_check(time_set_str)
			time_now = self.timestring_check(time_now_str)
			sys.stdout.write("\r" + "Now: %s" % time_now_str)
			sys.stdout.flush()
			self.time_compare(time_set, time_now)

	def time_compare(self, set_time, now_time):
		time_valid = False
		for i in range(0,6):
			if set_time[i] < now_time[i]:
				time_valid = False
				break
			elif set_time[i] > now_time[i]:
				time_valid = True
				break
			else:
				time_valid = True

		if time_valid:
			self.time_valid = time_valid
			if set_time == now_time:
				self.Trigger = True
				print("\nTime out!\n")
		else:
			self.time_valid = time_valid
			print("\nSet time is invalid now!")

	def input_time_string(self):
		Today = datetime.datetime.now().strftime('%Y-%m-%d')
		set_time_default = '%s 22:28:30' % Today
		time_str = input()
		time_str_check = self.timestring_check(time_str)
		if time_str_check == AtomTime:
			time_str = set_time_default
		return time_str

	def get_time_string(self, time_get_str):
		self.timing_routine(time_get_str)

def main():
	clockset = TimingRoutine()
	time_set_str = clockset.input_time_string()
	clockset.timing_routine(time_set_str)



if __name__ == '__main__':
	main()

	#!--get_time_string() is API for other program. 
	#Following line is for testing this API.--!

	# time_set_str = '2017-9-6 22:25:00'
	# clockset = TimingRoutine()
	# clockset.get_time_string(time_set_str)

