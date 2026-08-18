e, m, d = map(int, input().split())

q = []
nq = []
g = []

r = 0

# Alunos que querem ficar juntos
for i in range(m):
    q.append(list(map(int, input().split())))

# Alunos que não querem ficar juntos
for i in range(d):
    nq.append(list(map(int, input().split())))

# Grupos de alunos
for i in range(e // 3):
    g.append(list(map(int, input().split())))

# Verificação dos que querem ficar juntos
for dupla in q:
    juntos = False
    for grupo in g:
        if dupla[0] in grupo and dupla[1] in grupo:
            juntos = True
            break
        else:
            r += 1

# Verificação dos que não querem ficar junto
for dupla in nq:
    for grupo in g:
        if dupla[0] in grupo and dupla[1] in grupo:
            r += 1
            break

print(r)