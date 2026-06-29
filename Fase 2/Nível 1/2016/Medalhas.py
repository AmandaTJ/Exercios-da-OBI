t1 = int(input())
t2 = int(input())
t3 = int(input())
primeiro = 0
segundo = 0
terceiro = 0
if t1 < t2 and t1 < t3:
    primeiro = t1 = 1
    if t2 < t3:
        segundo = t2 = 2
        terceiro = t3 = 3
    else:
        segundo = t3 = 3
        terceiro = t2 = 2
elif t2 < t1 and t2 < t3:
    primeiro = t2 = 1
    if t1 < t3:
        segundo = t1 = 2
        terceiro = t3 = 3
    else:
        segundo = t3 = 3
        terceiro = t1 = 2
elif t3 < t1 and t3 < t2:
    primeiro = t3 = 1
    if t1 < t2:
        segundo = t1 = 2
        terceiro = t2 = 3
    else:
        segundo = t2 = 3
        terceiro = t1 = 2
print(t1)
print(t2)
print(t3)