n = int(input())
passes = list(map(int, input().split()))

time1 = 0
time2 = 0

for i in range(n - 1):

    if passes[i] > 0 and passes[i + 1] > 0:
        time1 += 1

    elif passes[i] < 0 and passes[i + 1] < 0:
        time2 += 1

print(time1)
print(time2)
