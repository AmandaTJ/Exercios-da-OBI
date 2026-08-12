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

for grupo in g:
    for g[grupo] in q:
        if g[grupo] != m[g[grupo]]:
            r += 1
for grupo in g:
    for g[grupo] in nq:
        if g[grupo] == nq[g[grupo]]:
            r += 1

print(r)