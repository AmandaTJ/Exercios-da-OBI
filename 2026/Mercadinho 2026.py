n = int(input())
idades = list(map(int, input().split()))
segundos = 0
nidosos = 0
for idade in idades:
    if idade >= 60:
        segundos = max(segundos, nidosos)
    else:
        nidosos += 1
print(segundos)
