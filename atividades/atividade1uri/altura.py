import math

def countingSort(A):
    # encontra o max
    maxElement = max(A)
    C = [0] * (maxElement + 1)

    # contar os elementos
    for i in range(maxElement + 1):
        C[i] = A.count(i)

    result = []

    # preencher array result
    for i in range(len(C)):
        for j in range(C[i]):
            result.append(i)
    return result

nc = int(input())

while nc:
    nc -= 1
    n = int(input())
    vetor = list(map(int, input().split()))

    vetor = countingSort(vetor)

    print(' '.join(str(x) for x in vetor))