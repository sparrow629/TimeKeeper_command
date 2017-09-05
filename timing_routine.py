import datetime
import time
import re

AtomTime = '2017-9-9 24:60:60'
Str_format = 'Set time like format as 2017-9-9 24:60:60'
Str_Invalid = 'Contain invalid time'
Str_illegal = 'Illegal time format!'

class TimingRoutine():
	"""docstring for TimingRoutine"""
	def __init__(self):
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
				month = int(times[1])
				day = int(times[2])
				hour = int(times[3])
				minute = int(times[4])
				second = int(times[5])
				set_time = (year, month, day, hour, minute, second)
			except:
				print(Str_Invalid)
				set_time = AtomTime

		else:
			print(Str_illegal)
			set_time = AtomTime
		
		return set_time

	def show_now(self):
		self.now = datetime.datetime.now()
		time_now = self.now.strftime('%Y-%m-%d %H:%M:%S')
		print(time_now)
		return time_now

	def timingroutine(self,time_set_str):
		Trigger = False
		while not Trigger:
			time_now_str = self.show_now()
			time.sleep(1)
			time_set = self.timestring_check(time_set_str)
			time_now = self.timestring_check(time_now_str)
			print("%s %s " % (time_set[3:], time_now[3:]))
			if time_set == time_now:
				Trigger = True
				print("Time out!")


if __name__ == '__main__':
	time_set_str = '2017-9-5 23:45:0'
	clockset = TimingRoutine()
	clockset.timingroutine(time_set_str)
