N, M = map(int, input().split()) # n = linhas e m = colunas 
tabuleiro = [] # matriz do tabulerio
for i in range(N):
    tabuleiro.append(list(input())) # adiciona a descrição do tabuleiro na matriz

K = int(input())# numero de tiros
tiros = [[False] * M for i in range(N)] # matriz de tiros em cima do tabuleiro, inicialmente todos não foram atingidos

for i in range(K): # adiciona cada tiro na matriz de tiros
    L, C = map(int, input().split()) # coordenadas do tiro
    tiros[L-1][C-1] = True # subtrai um pq as coordenadas do enunciado são inicam em 1 mas os indices no py começam em 0

def dfs(l, c): # funão de busca em profundidade pra encontra os navios
    tabuleiro[l][c] = '.' # marca a posição como visitada
    navio = [(l, c)]
    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)] # cada direção possivel ser achar um navio

    for dl, dc in direcoes: # percorre cada direção
        nl = l + dl # calcula a nova linha
        nc = c + dc # calcula a nova coluna
        if 0 <= nl < N and 0 <= nc < M: # pra não sair do tabuleiro
            if tabuleiro[nl][nc] == '#': # marca o navio
                navio += dfs(nl, nc)
    return navio


resposta = 0

for i in range(N): # para acahar os navios destruidos
    for j in range(M):
        if tabuleiro[i][j] == '#':
            partes = dfs(i, j)
            destruido = True
            for l, c in partes:
                if not tiros[l][c]:
                    destruido = False
                    break
            if destruido:
                resposta += 1

print(resposta)
# esse é complexo para a primeira fase, mas é só uma busca em profundidade e depois verificar se todas as partes do navio foram atingidas
# não vou me atrever a fazer isso em Java mas nem que seja sob pena de morte
# esse nem deu 100%, não consegui resolver o prolbema, aparentemente ele está excedendo o tempo limite de alguma subtarefa, mas não sei qual