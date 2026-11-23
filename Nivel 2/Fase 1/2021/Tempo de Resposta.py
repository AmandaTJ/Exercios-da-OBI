# R X indica que uma mensagem foi recebida do amigo X.
# E X indica que uma mensagem foi enviada ao amigo X.
# T X indicando que X segundos se passaram entre o evento anterior e o evento posterior a esse registro.
n = int(input())

tempo = 0
avanco = 1  # Quanto o tempo vai andar no próximo evento (1s por padrão)

# Listas para guardar dados dos amigos (índices de 0 a 100)
chegada = [-1] * 101     # -1 indica que não há mensagem esperando resposta
tempo_total = [0] * 101  # Soma dos tempos de resposta de cada amigo
apareceu = [False] * 101 # Marca quais amigos participaram da conversa

for _ in range(n):
    tipo, x = input().split()
    x = int(x)

    if tipo == "T":
        avanco = x
    else:
        tempo += avanco
        avanco = 1  # Volta para o padrão de 1 segundo
        apareceu[x] = True

        if tipo == "R":
            chegada[x] = tempo
        elif tipo == "E":
            tempo_total[x] += tempo - chegada[x]
            chegada[x] = -1  # Marca que a mensagem já foi respondida

# Imprime os resultados em ordem crescente (do amigo 1 ao 100)
for amigo in range(1, 101):
    if apareceu[amigo]:
        if chegada[amigo] != -1:  # Ainda tem mensagem sem resposta
            print(amigo, -1)
        else:
            print(amigo, tempo_total[amigo])
# pedi para IA comentar
# creditos: Gemini