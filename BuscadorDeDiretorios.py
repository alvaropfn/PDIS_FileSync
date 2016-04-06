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
        except Exception as excecao:
            print(excecao)

    def pathSearch(self, oldPath):
        pdis_sinc = open("pdis_sinc.txt", "a")

        #create new threads to start search in subdirectories
        for dir in listDirs(oldPath):
            newPath = os.path.join(oldPath, dir)
            id = self.id+1

            try:
                nt = searcherThread(newPath, id)
                nt.start()
            except:
                print("erro na execução do método searcherThread")

            #print all files in this directory
        for file in listFiles(oldPath):
            novoCaminho = os.path.join(oldPath, file)
            # /caminho/arquivo.tipo,013291301932\n
            pdis_sinc.write(novoCaminho + "\t" + str(os.stat(novoCaminho).st_mtime) + "\n")

        pdis_sinc.close()

'''searcherThread ends'''
########################################################
listDirs = lambda path: [d.name for d in os.scandir(path)
                         if d.is_dir()]
listFiles = lambda path: [f.name for f in os.scandir(path)
                          if f.is_file()]

ps = searcherThread(myPath)
ps.start()
