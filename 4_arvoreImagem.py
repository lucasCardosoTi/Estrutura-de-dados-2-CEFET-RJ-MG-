# Função imagem de uma HEAP

def nivel(i=0):
    return 2**i

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