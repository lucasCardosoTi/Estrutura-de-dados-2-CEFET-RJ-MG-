# Calcula o nivel       
def nivel(i=0):
    return 2**i
    
def eh_cheia(n):
    i = 0
    cheia = 0
    while True:
        cheia = cheia + nivel(i)
        if n == cheia:
            print("Cheia")
            break
        elif n < cheia:
            print("Arvore Incompleta!")
            break
        i = i + 1

B = [0, 100, 30, 10,]
eh_cheia(len(B)-1)
