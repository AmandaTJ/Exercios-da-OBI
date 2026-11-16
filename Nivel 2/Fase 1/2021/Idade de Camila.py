# Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.
# cibele > Camila > Celeste
n1 = int(input())
n2 = int(input())
n3 = int(input())

ic = 0 # idade de camila

if n1 >= n2 and n1 <= n3 or n1 <= n2 and n1 >= n3:
    ic = n1

elif n2 >= n1 and n2 <= n3 or n2 <= n1 and n2 >= n3:
    ic = n2

else:
    ic = n3

print(ic)