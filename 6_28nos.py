## Retorna a quantidade de elementos por nível
def nivel(i=0):
    return 2**i

## Mostra a largura dos níveis
def mostra_largura(A):
    check = 1                           # Armazena a última posição do laço
    k = 0                               # Variável auxiliar. Utilizada para passar o nível
    while check < len(A)-1:
        n = nivel(k)                    # Passa o nível para função que retorna a quantidade de elementos
        for i in range(check, 2*n):     
            if i < len(A): 
                print(A[i]," ",end="")  # Apresetanção dos elementos por nível
        print("\n")
        check = check + n    # Check recebe o N para no próximo laço iniciar na posição de parada do laço atual
        k = k + 1 


def altura(B):
    total = 0 
    altura = 0
    while total < len(B)-1:    # inicia o laço verificando o tamanho da lista 
        total += nivel(altura) # Recebe número de elementos para o próximo laço 
        altura += 1      # Contador da altura 
    return altura

B = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
mostra_largura(B)
print("Altura: ", altura(B))