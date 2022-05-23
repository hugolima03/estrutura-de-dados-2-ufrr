N, K = [int(x) for x in input().split()]

names = []

for i in range(int(N)):
  names.append(input())

names.sort()

print(names[int(K)-1])