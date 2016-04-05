import threading
import time

class ThreadTest(threading.Thread):

	def __init__(self, name, delay):
		threading.Thread.__init__(self)
		self.name = name
		self.delay = delay

	def printTime(self):
		count = 0
		while count < 5:
			time.sleep(self.delay)
			count+=1
			print(self.name + "-" + str(time.ctime()))

	def run(self):
		self.printTime()
		print(self.name + ' ending activity')
		exit()