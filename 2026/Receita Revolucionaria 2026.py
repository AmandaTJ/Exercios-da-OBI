P = int(input())
O = int(input())
D = 0
while P >= 2 and O >= 4:
    D += 1
    P -= 2
    O -= 4
print(D)
