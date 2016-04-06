import os

#myPath = input("entre com o caminho a ser pesquisado")
myPaths = ["/home/jmatiasn/Git/",
           "/home/jmatiasn/Downloads/multcast/"]

# recebe um array com 2 strings de paths de arquivos
class ComparadorDeArquivos(object):

    def __init__(self, filepaths):
        self.filePath1 = filepaths[0]
        self.filePath2 = filepaths[1]
        try:
            self.statbuf1 = os.stat(self.filePath1).st_mtime
            print(self.statbuf1)
        except:
            print("Arquivo1 não encontrado")
        try:
            self.statbuf2 = os.stat(self.filePath2).st_mtime
            print(self.statbuf2)
        except:
            print("Arquivo2 não encontrado")

    def run(self):
        try:
            self.compararMaisRecente(self.statbuf1, self.statbuf2)
        except :
            print("erro ao comparar 2 caminhos")

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
