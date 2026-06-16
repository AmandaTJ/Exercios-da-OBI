E = int(input())
D = int(input())
if (E != D) and (0 <= E <= 5) and (0 <= D <= 5):
    if E > D:
        print(E + D)
    else:
        print(2 * (D - E))
    