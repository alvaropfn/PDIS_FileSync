from Receiver import *
from Sender import *
import threading

receiver = Receiver()
sender = Sender()

try:
	print('starting receiver')
	#threading._start_new_thread(receiver.run())
	print('starting sender')
	#threading._start_new_thread(sender.run())
except:
	print('thread error')