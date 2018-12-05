from pilha import Pilha
import time

pilha = Pilha()
resposta = open("resposta.txt","w")

inicio = time.time()
arquivo = open("insert1.txt")
for linha in arquivo:
    linha = linha.rstrip()
    pilha.push(linha)
fim = time.time()

resposta.write("O tempo de execução foi ")
resposta.write(str(fim - inicio))
resposta.close()
