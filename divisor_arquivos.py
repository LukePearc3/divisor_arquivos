import sys
def usage():
    try:
        sys.argv[1]
    except Exception as erro:
        print("Usage: ./divisor.py \"arquivo\" \"quantidade_divisoes\"")
        exit(0)
def validacao():
    try:
        file = open(str(sys.argv[1]), "r")
        file.close()
    except Exception as erro1:
        print("Nao e um arquivo de texto")
        print("Usage: ./divisor.py \"arquivo\" \"quantidade_divisoes\"")
        exit(1)

def tamanho_arquivo(arquivo):
    tam = 0
    with open(arquivo,"r") as f:
        for i in f:
            tam +=1
    return tam

def criar_arquivos(arquivo,divisoes):
    for qtde in range(divisoes):
        file = open(arquivo + "-parte" + str(qtde + 1) + ".txt", "w")
        file.close()

def dividir_arquivos(arquivo,divisoes):
    tamanho_usuario = divisoes
    quantidade_linhas = tamanho_arquivo(arquivo)
    inicio = 0
    fim = int (quantidade_linhas / tamanho_usuario + 1)
    with open(arquivo, "r") as f:
        for qtde in range(tamanho_usuario):
            with open(arquivo + "-parte" + str(qtde + 1) + ".txt", "a") as g:
                for linha in range(quantidade_linhas)[inicio:fim]:
                    palavra = f.readline()
                    g.write(palavra)
                inicio = int (inicio + (quantidade_linhas / tamanho_usuario))
                fim = int (fim + (quantidade_linhas / tamanho_usuario) + qtde)
def main():
    usage()
    validacao()
    print("Lendo arquivo")
    print("Qtde linhas: " + str(tamanho_arquivo(str(sys.argv[1]))))
    print("Gerando arquivos")
    criar_arquivos(str(sys.argv[1]), int(sys.argv[2]))
    dividir_arquivos(str(sys.argv[1]), int(sys.argv[2]))
    print("Concluido")
    print("By: LukePearc3")

main()