A = int(input())
B = int(input())
C = int(input())
D = int(input())

print(min(
    abs((A + B) - (C + D)), # Deixa a saída positiva
    abs((A + C) - (B + D)),
    abs((A + D) - (B + C))
))