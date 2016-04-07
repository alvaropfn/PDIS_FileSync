from urllib import error

import os, threading, time

#myPath = input("entre com o caminho a ser pesquisado")
myPath = "/home/alvaro/Workspace/FileSearcher"

class searcherThread(threading.Thread):
	def __init__(self, path, id = 0):
		threading.Thread.__init__(self)
		self.path = path
		self.id = id

	def run(self):
		try:
			print(self.getName(), "as born!")
			self.pathSearch(self.path)
		except :
			print("paw")

	def pathSearch(self, oldPath):
		#create new threads to start search in subdirectories
		for dir in listDirs(oldPath):
			newPath = os.path.join(oldPath, dir)
			#self._tstate_lock()
			id = self.id + 1

			try:
				nt = searcherThread(newPath, id)
				nt.start()
			except:
				print("porra!")

		#print all files in this directory
		for file in listDirs(oldPath):
			print(self.getName(), os.path.join(oldPath, file))

		print(self.getName(), "as finished!")
'''searcherThread ends'''
########################################################
listDirs = lambda path: [d for d in os.listdir(path)
                         if os.path.isdir(d)]
listFiles = lambda path: [f for f in os.listdir(path)
                          if os.path.isfile(f)]

class searchThread(threading.Thread):
	def __init__(self, path, id = 0):
		threading.Thread.__init__(self)
		self.path = path
		self.id =id


ps = searcherThread(myPath)
ps.start()