import os
import ComparadorDeArquivos

class ComparadorDeListas(object):

    #Recebe um array com 2 nomes de arquivo
    # [0] = arquivo do cliente
    # [1] = arquivo do servidor
    def __init__(self, fileNames):
        #Cliente
        self.fileName1 = fileNames[0]
        #Servidor
        self.fileName2 = fileNames[1]

    def run(self):
        try:
            self.gerarListaAAtualizar()
        except Exception as excecao:
            print("run " + excecao)

    def gerarListaAAtualizar(self):
        try:
            #Abre arquivo para leitura
            file1 = open(self.fileName1, "r")
            #Obtem a lista de linhas
            lines1 = file1.readlines()
            file1.close()
            file2 = open(self.fileName2, "r")
            lines2 = file2.readlines()
            file2.close()

            #Para cada linha no arquivo do cliente, verifica em todas as linhas do arquivo do servidor
            #se ele se encontra tambem no servidor
            for line1 in lines1:
                isArquivoUnico = True
                path1 = line1.split(",", 1)
                for line2 in lines2:
                    path2 = line2.split(",", 1)
                    if path1[0] == path2[0]:
                        isArquivoUnico = False
                        self.compararArquivos(path1[0], path2[0])
                if isArquivoUnico == True:
                    self.arquivoAAtualizar("servidorAAtualizar.txt", path1[0], os.stat(path1[0]).st_mtime)

            #Procedimento inverso apenas para identificar se ha arquivos unicos no servidor
            for line2 in lines2:
                isArquivoUnico = True
                path2 = line2.split(",", 1)
                for line1 in lines1:
                    path1 = line1.split(",", 1)
                    if path1[0] == path2[0]:
                        isArquivoUnico = False
                if isArquivoUnico == True:
                    self.arquivoAAtualizar("clienteAAtualizar.txt", path2[0], os.stat(path2[0]).st_mtime)

        except Exception as excecao:
            print("gerarListaAAtualizar " + excecao)

    def compararArquivos(self, filePath1, filePath2):
        try:
            #Cliente
            statbuf1 = os.stat(filePath1).st_mtime
            #Servidor
            statbuf2 = os.stat(filePath2).st_mtime
            if statbuf1 > statbuf2:
                #Arquivo no cliente mais recente
                self.arquivoAAtualizar("clienteAAtualizar.txt", filePath1, statbuf1)
            if statbuf1 < statbuf2:
                #Arquivo no servidor mais recente
                self.arquivoAAtualizar("servidorAAtualizar.txt", filePath2, statbuf2)
        except Exception as excecao:
            print("compararArquivos " + excecao)

    #Abre arquivo (senao houver, cria)
    #Armazena formato padrao (caminho + "," + tempo de ultima modificacao + "\n")
    #Fecha arquivo
    def arquivoAAtualizar(self, nomeArquivo, path, statbuf):
        arquivoAAtualizar = open(nomeArquivo, "a")
        arquivoAAtualizar.write(path + "," + str(statbuf) + "\n")
        arquivoAAtualizar.close()

'''ComparadorDeArquivos ends'''

teste = ComparadorDeListas(["pdis_sinc.txt", "pdis_sin.txt"])
teste.run()
