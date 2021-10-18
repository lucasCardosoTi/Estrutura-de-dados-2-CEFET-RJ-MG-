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

B = [0,1,2,3,4,5,6,7,8,9]
mostra_largura(B)