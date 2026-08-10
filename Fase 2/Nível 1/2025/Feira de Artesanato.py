
# cliente decidido: compra o objeto do tipo desejado que possui o menor preço. Se tiver mais de um objeto com o mesmo preço, compra qualquer um delse. Se não tiver o tipo deseja, vai embora.
# cliente indeciso: compra o objeto de menor preço, se tiver mais de um objeto com o mesmo preço, compra o com o tipo minimo.

# Exemplo de entrada:
# 8 10
# 4 2 3 1 10 1 1 4 
# 34 50 156 81 97 12 3 3 
# 7
# 0 1 0 1 5 4 1
# resposta = 133

n, t = map(int, input().split()) # numero de objetos e numero de tipos

tipos = list(map(int, input().split())) # lista com os tipos de cada objeto
precos = list(map(int, input().split())) # lista com os preços

nc = int(input()) # total de clientes
tclientes = list(map(int, input().split())) # lista com os tipos de objetos que o cliente quer comprar, se 0, o clente é indeciso

disponivel = [True] * n # cria uma lista que representa o estoque, sendo true para disponível e false para indisponível. Inicialmente todos os objetos estão disponíveis.

total = 0 # preço total

for t in tclientes:

    provavel = -1

    if t != 0:
        # Cliente decidido
        for i in range(n): # cria uma lista com os objetos disponiveis e percorre um a um.
            if disponivel[i] and tipos[i] == t:
                if provavel == -1 or precos[i] < precos[provavel]:
                    provavel = i
    else:
        # Cliente indeciso
        for i in range(n): # cria uma lista com os objetos disponiveis e percorre um a um.
            if disponivel[i]: # verifica se o objeto está disponível(está em true)
                if (provavel == -1 or precos[i] < precos[provavel] or (precos[i] == precos[provavel] and tipos[i] < tipos[provavel])):
                    provavel = i

    # Se o cliente comprou um objeto.
    if provavel != -1:
        total += precos[provavel]
        disponivel[provavel] = False # tira o objeto do estoque, marcando como indisponível(false)

print(total)