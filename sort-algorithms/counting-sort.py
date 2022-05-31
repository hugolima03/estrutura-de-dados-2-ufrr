def countingSort(A):
    # encontra o max
    maxElement = max(A)
    C = [0] * (maxElement + 1)

    # contar os elementos
    for i in range(maxElement):
        C[i] = A.count(i)

    result = []

    # preencher array result
    for i in range(len(C)):
        for j in range(C[i]):
            result.append(i)
    return result

print(countingSort([8,4,0,2,8,0,3,9,3,0,1]))

# A = [8,4,0,2,8,0,3,9,3,0,1]
# C = [3,1,1,2,1,0,0,0,2,1]
# result = [0,0,0,1,2,3,3,4,8,8,9]
