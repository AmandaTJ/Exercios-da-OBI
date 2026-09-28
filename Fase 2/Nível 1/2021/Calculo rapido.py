s = int(input()) # número que a soma deve ter
a = int(input()) # primeiro inteiro do intervalo
b = int(input()) # ultimo inteiro do intervalo
quantidade = 0

for n in range(a, b + 1):
    soma = sum(int(digito) for digito in str(n))

    if soma == s:
        quantidade += 1

print(quantidade)