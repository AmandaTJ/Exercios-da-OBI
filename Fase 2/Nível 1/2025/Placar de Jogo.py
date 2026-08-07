entradap = list(map(int, input().split()))
P = entradap[0]
paulo = entradap[1:]

entradac = list(map(int, input().split()))
C = entradac[0]
camila = entradac[1:]

gols = [0] * 101
for m in paulo:
    gols[m] = 1
for m in camila:
    gols[m] = 2
sp = 0
sc = 0

print(sp, sc)

for minuto in range(1, 101):
    if gols[minuto] == 1:
        sp += 1
        print(sp, sc)
    elif gols[minuto] == 2:
        sc += 1
        print(sp, sc)


