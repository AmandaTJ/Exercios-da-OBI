n, k = map(int, input().split())
notas = list(map(int, input().split()))

notas.sort(reverse=True)
print(notas[k-1])