n = int(input()) # números de caracteres da primeira palavra
p = input() # caracteres da primeria palavra

m = int(input()) # numero de caracteres da segunda palavras
s = input() # caraceres da segunda palavras

i = 0 # conta a quantidade de letras da do prefixo comum

while i < n and i < m and p[i] == s[i]:
    i += 1

print(i)