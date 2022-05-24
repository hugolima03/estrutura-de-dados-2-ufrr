def count_sort_letters(array, size, col, base, max_len):
  """ Rotina auxiliar para executar o counting sort com base na coluna 'col' """
  output   = [0] * size
  count    = [0] * (base + 1) # One addition cell to account for dummy letter
  min_base = ord('a') - 1 # ord() retorna o valor unicode da string e subtrai 1 

  for item in array: # generate Counts
    # get column letter if within string, else use dummy position of 0
    letter = ord(item[col]) - min_base if col < len(item) else 0
    count[letter] += 1

  for i in range(len(count)-1):   # Accumulate counts
      count[i + 1] += count[i]

  for item in reversed(array):
    # Get index of current letter of item at index col in count array
    letter = ord(item[col]) - min_base if col < len(item) else 0
    output[count[letter] - 1] = item
    count[letter] -= 1

  return output

def radix_sort_letters(array, max_col = None):
  if not max_col:
    max_col = len(max(array, key = len)) # Encontrando a string mais longa em uma lista de strings e retornando o tamanho dela.

  for col in range(max_col-1, -1, -1): # len(array) - 1 até 0
    array = count_sort_letters(array, len(array), col, 26, max_col)

  return array

# vetor = input().split()

with open('dna_seq.txt') as f:
    contents = f.read()
    dna = (list(contents.replace('\n','').split(' ')))
    print(radix_sort_letters(dna))

f.close()