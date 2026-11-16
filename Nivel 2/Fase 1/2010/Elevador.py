# uma facil pelo menos
n, c = map(int, input().split()) # n = numero de leituras e c = capacidade do elevador
controle = False
p = 0 # numero de pessoas
for i in range(n):
    s, e = map(int, input().split()) # s = numero que sairam e p = numero que entraram
    p = p - s + e # atualiza a quantidade de gente no elevador
    if p > c:
        controle = True

print("S" if controle else "N")
# esse da pra fazer em java mas to com preguiça hj