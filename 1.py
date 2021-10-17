HEAP = [0, 100, 19, 36, 17, 3, 25, 1, 2, 7]

#Funcao para ver se a arvore eh HEAP, slide do professor
def eh_heap(A):
  for i in range(2, len(A)):
    if A[i] > A[i//2]:
      return false
  return true

print(eh_heap(HEAP))