# Primeira implementacao
# fileName = "/home/jmatiasn/Git/PDIS_FileSync/BuscadorDeDiretorios.py"
# statbuf = os.stat(fileName)
# print "Buscador"
# print "Modification time:",statbuf.st_mtime

# Segunda implementacao
# import os.path, time
# filename = "/home/jmatiasn/Git/PDIS_FileSync/BuscadorDeDiretorios.py"
# print "last modified: %s" % time.ctime(os.path.getmtime(filename))

import os

#myPath = input("entre com o caminho a ser pesquisado")
myPaths = ["/home/jmatiasn/Git/PDIS_FileSync/BuscadorDeDiretorios.py",
                        "/home/jmatiasn/Git/PDIS_FileSync/ComparadorDeArquivos.py"]

# recebe um array com 2 strings de paths de arquivos
class ComparadorDeArquivos(object):

    def __init__(self, filepaths):
        self.filePath1 = filepaths[0]
        self.filePath2 = filepaths[1]
        self.statbuf1 = os.stat(self.filePath1).st_mtime
        self.statbuf2 = os.stat(self.filePath2).st_mtime

    def run(self):
        try:
            self.compararMaisRecente(self.statbuf1, self.statbuf2)
        except :
            print("erro")

    def compararMaisRecente(self, statbuf1, statbuf2):
        if statbuf1 > statbuf2:
            print(self.filePath1)
        if statbuf2 > statbuf1:
            print(self.filePath2)
        if statbuf1 == statbuf2:
            print("iguais")

'''ComparadorDeArquivos ends'''

teste = ComparadorDeArquivos(myPaths)
teste.run()
