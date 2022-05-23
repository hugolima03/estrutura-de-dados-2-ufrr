N = int(input())

numbers = []
count = 0
iterator = 0

for i in range(N):
    numbers.append(int(input()))

numbers.sort()

while count < len(numbers):
    occurrences = numbers.count(numbers[count + iterator])
    if occurrences:
      print(numbers[count], "aparece", occurrences, "vez(es)")
      count += occurrences
      iterator = 0
    else:
      iterator += 1