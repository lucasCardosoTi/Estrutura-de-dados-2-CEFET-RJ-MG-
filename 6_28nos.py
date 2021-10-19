def nivel(i=0):
    return 2**i

def mostra_largura(A):
    check = 1
    k = 0
    while check < len(A)-1:
        n = nivel(k)
        for i in range(check, 2*n):
            if i < len(A):
                print(A[i]," ",end="")
            
        print("\n")
        check = check + n
        k = k + 1

#Função retorna altura arvore
def altura(A):
    altura = 0
    check = 1
    k = 0
    while check < len(A)-1:
        n = nivel(k)
        check = check + n
        k = k + 1
        altura += 1

    print(altura)

def altura(B):
    i = 0
    total = 0
    altura = 0
    while total < len(B)-1:
        n = nivel(altura)
        total = total + n
        altura = altura + 1
    return altura

B = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
mostra_largura(B)
print("Altura: ", altura(B))