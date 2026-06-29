D = int(input()) # valor da diaria no dia 1
A = int(input()) # valor do acrecimo
N = int(input()) # dia da chegada
if N <= 15:
    valor = D + (N - 1) *A #Preço da diaria se tiver aumento
else:
    valor = D + 14 * A #Preço da diara se não tiver aumento
total = valor * (31 - N + 1) #Preço total
print(total)