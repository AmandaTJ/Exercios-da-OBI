A = int(input())#idade da primeira pessoa
B = int(input()) #idade da segunda pessoa
valor = 0
if A <= 17:
    valor += 15
elif 18 <= A <= 59:
    valor += 30
elif A >= 60:
    valor += 20
if B <= 17:
    valor += 15
elif 18 <= B <= 59:
    valor += 30
elif B >= 60:
    valor += 20
print(valor)