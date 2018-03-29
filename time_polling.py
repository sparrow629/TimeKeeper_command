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

	def time_polling_duration(self, duraiton):
		date = datetime.date(*map(int, self.endtime.split('-')))
		count = duraiton
		while not count == 0:
			self.func(date)
			date = date - datetime.timedelta(days = 1)
			count -= 1

def printer(date):
	print date

def show():
	starttime = '2018-02-28'
	endtime = '2018-03-09'
	polling = TimePolling(printer, starttime, endtime)
	# polling.time_polling()
	polling.time_polling_duration(20)

if __name__ == '__main__':
	show()