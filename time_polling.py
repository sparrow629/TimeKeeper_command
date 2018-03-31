# -*- coding: utf-8 -*-
import datetime

class TimePolling(object):
	"""docstring for ClassName"""
	def __init__(self, func, starttime, endtime):
		
		self.func = func
		self.starttime = starttime
		self.endtime = endtime 
		
	def time_polling(self):
		date = datetime.date(*map(int, self.starttime.split('-')))
		endtime = datetime.date(*map(int, self.endtime.split('-')))
		while not date == endtime:
			self.func(date)
			date = date + datetime.timedelta(days = 1)

	def time_polling_duration(self, duration):
		date = datetime.date(*map(int, self.endtime.split('-')))
		count = duration
		while not count == 0:
			self.func(date)
			date = date - datetime.timedelta(days = 1)
			count -= 1

	def yesterday(self):
		yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
		self.func(yesterday)

	def this_week(self):
		date = datetime.datetime.now()
		duration = date.weekday() + 1
		count = duration
		while not count == 0:
			self.func(date.strftime('%Y-%m-%d'))
			date = date - datetime.timedelta(days=1)
			count -= 1

def printer(date):
	print date


def show():
	starttime = '2018-02-28'
	endtime = '2018-03-09'
	polling = TimePolling(printer, starttime, endtime)
	# polling.time_polling()
	# polling.time_polling_duration(20)
	# polling.yesterday()
	polling.this_week()

if __name__ == '__main__':
	show()