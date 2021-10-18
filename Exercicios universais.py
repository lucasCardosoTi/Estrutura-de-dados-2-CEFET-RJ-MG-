# Caio Ciriaco
# Lucas de Mendonça
# CEFET/RJ - Maria da Graça
# Sistema de Informação
# Estrutura de Dados II - Arvore HEAP
# Professor Ronilson Rodrigues Pinho

#Funcao para ver se a arvore eh HEAP, slide do professor
def eh_heap(A):
  for i in range(2, len(A)):
    if A[i] > A[i//2]:
      return False
  return True
      
# Calcular o numero de elementos por nivel      
def nivel(i=0):
    return 2**i

# Compara o numero de elementos com o nivel
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

# Vetor de exemplo
B = [0, 100, 30, 10, 5]
eh_cheia(len(B)-1)

# Função imagem de uma HEAP
def heap_imagem(A):
    total = 0
    imagem = A.copy()
    i = 1
    while total < len(A)//2:
        n = nivel(i)
        for k in range(0,n):
            imagem[n+k] = A[2*n + (-1)*k - 1]
        total = total + n
        i = i + 1
    return imagem

HEAP = [0, 1, 2, 3]
HEAP_imagem = heap_imagem(HEAP)
print("HEAP  : ",HEAP)
print("IMAGEM: ",HEAP_imagem)

HEAP = [0, 1, 2, 3, 4, 5, 6, 7]
HEAP_imagem = heap_imagem(HEAP)
print("HEAP  : ",HEAP)
print("IMAGEM: ",HEAP_imagem)

HEAP = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
        18,19,20,21,22,23,24,25,26,27,28,29,30,31]
HEAP_imagem = heap_imagem(HEAP)
print("HEAP  : ",HEAP)
print("IMAGEM: ",HEAP_imagem)
