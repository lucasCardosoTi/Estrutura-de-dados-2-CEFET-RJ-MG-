# Calcula o nivel       
def nivel(i=0):
    return 2**i

# Compara o numero de elementos com o nivel
def eh_cheia(n):
    i = 0
    cheia = 0
    while True:
        cheia = cheia + nivel(i) # Cheia = numero de elementos do nivel(i)
        if n == cheia: # Verifica se o tamanho do vetor é igual ao número de elementos total da função nivel
            print("Arvore Cheia")
            break
        elif n < cheia: #  Verifica se o tamanho do vetor é menor ao número de elementos total da função nivel
            print("Arvore Incompleta!")
            break
        i = i + 1

# Vetor de exemplo
B = [0, 1,2,3,4,5,6,7]
eh_cheia(len(B)-1)