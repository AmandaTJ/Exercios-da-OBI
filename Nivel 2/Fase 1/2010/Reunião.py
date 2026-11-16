n, m = map(int, input().split()) # n = quantidade de cidades e m = quantidade de estradas

inf = float('inf') # coloca infinito pq inicialmente não tem nenhum valor de estrada
dist = [[inf]*n for i in range(n)] # matriz para agrupar as cidades

for i in range(n):
    dist[i][i] = 0 # a distancia da cidade pra ela mesma é 0

for i in range(m): # registra as estradas na matriz de distancias
    u, v, w = map(int, input().split()) # u = primeira cidade, v = segunda cidade, w = comprimento da estrada
    dist[u][v] = min(dist[u][v], w) # registra os dois caminhos
    dist[v][u] = min(dist[v][u], w)

for k in range(n): # aqui complica, mas é simples até. I =  cidade de origem, j = cidade de destino e k = cidade intermediaria
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) # verifica se é melhor ir direto ou parar na cidade k

resposta = inf

for i in range(n):
    maior = max(dist[i]) # encontr a mairo distancia de entre a cidade i e as outras
    resposta = min(resposta, maior) # verifica a menor

print(resposta)
# esse deu trabalhos