import random
import numpy as np

N, A, B = map(int, input().split())

n = 1000000 
sumcont = 0
para = False
for i in range(n):
    if A == B:
        para = True
        print(f'{N / 10:.5f}')
        break
    contador = 0
    figurinhas = 0
    ncomp = True
    while ncomp:
        figurinhas += random.choice(range(A,B+1))
        #figurinhas += np.random.randint(A, B + 1, size=1)[0]

        contador += 1
        if figurinhas >= N:
            sumcont += contador
            ncomp = False

if not para:
    print(f'{sumcont/n:.5f}')