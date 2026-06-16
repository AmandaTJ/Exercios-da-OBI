N = int(input())
P = int(input())
bacterias = 1
dias = 0
while bacterias * P <= N:
    dias += 1
    bacterias *= P
print(dias)