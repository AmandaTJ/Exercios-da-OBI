n, k = map(int, input().split()) # n é a dimensão do quadrado e k o númeor de pistas
for i in range(k):
    x, y, d = map(int, input().split()) # x e y são as coordenadas e d é a quantidade de passos do capitão

matriz = [[[0]*n for i in range(n)] for j in range(n)] # cria a matriz do quadrado
print(matriz) # printa a matriz do quadrado