#variaveis
# A minimo de leite
# B maximo de leite
# C capacidade da xicara/ total de café com leite
# D quantidade de café na xicara
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = C - D
if A <= P <= B:
    print("S")
else:
    print("N")
        