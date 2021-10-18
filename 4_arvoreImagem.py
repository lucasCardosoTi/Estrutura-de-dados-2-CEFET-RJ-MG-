

A = [0, 100, 30, 10, 6, 8, 15, 18, 19]
B = [0,1,2,3]
C = [0,1,2,3,4,5,6,7]

def arvoreImagem(A):
    img = []
    img.append(A[0])
    img.append(A[1])
    for i in range (1, len(A)):
        if(i*2+1 <= len(A) - 1):    
            img.append(A[i*2+1])
        if(i*2 <= len(A) - 1):
            img.append(A[i*2])
    
    return img

print("Arvore B:")
print(B)
print(arvoreImagem(B))
print("Arvore C:")
print(C)
print(arvoreImagem(C))