# Primeira implementacao
# from os import listdir
# for f in listdir("/home/jmatiasn/Git/PDIS_FileSync/"):
#     print(f)

# from urllib import error

import os, threading, time

#myPath = input("entre com o caminho a ser pesquisado")
myPath = "/home/jmatiasn/Git/"

class searcherThread(threading.Thread):
	def __init__(self, path, id = 0):
		threading.Thread.__init__(self)
		self.path = path
		self.id = id

	def run(self):
		try:
			self.pathSearch(self.path)
		except :
			print("erro")

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
				print("erro!")

        #print all folders in this directory
		for folder in listDirs(oldPath):
			print(self.getName(), os.path.join(oldPath, folder))

        #print all files in this directory
		for file in listFiles(oldPath):
			print(self.getName(), os.path.join(oldPath, file))

'''searcherThread ends'''
########################################################
listDirs = lambda path: [d for d in os.listdir(path)
                         if os.path.isdir(d)]
listFiles = lambda path: [f for f in os.listdir(path)
                          if not os.path.isdir(f)]

ps = searcherThread(myPath)
ps.start()
