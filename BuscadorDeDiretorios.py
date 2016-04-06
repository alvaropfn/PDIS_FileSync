import os, threading, time

#myPath = input("entre com o caminho a ser pesquisado")
myPath = "/home/jmatiasn/Git/PDIS_FileSync"

class searcherThread(threading.Thread):

    def __init__(self, path, id = 0):
        threading.Thread.__init__(self)
        self.path = path
        self.id = id

    def run(self):
        try:
            self.pathSearch(self.path)
        except :
            print("erro na execução do método pathSearch")

    def pathSearch(self, oldPath):
        #create new threads to start search in subdirectories
        for dir in listDirs(oldPath):
            newPath = os.path.join(oldPath, dir)
            #self._tstate_lock()
            id = self.id+1

            try:
                nt = searcherThread(newPath, id)
                nt.start()
            except:
                print("erro na execução do método searcherThread")

                #print all folders in this directory
        # for folder in listDirs(oldPath):
            # print(os.path.join(oldPath, folder))

            #print all files in this directory
        for file in listFiles(oldPath):
            print(os.path.join(oldPath, file))

'''searcherThread ends'''
########################################################
listDirs = lambda path: [d.name for d in os.scandir(path)
                         if d.is_dir()]
listFiles = lambda path: [f.name for f in os.scandir(path)
                          if f.is_file()]

ps = searcherThread(myPath)
ps.start()
