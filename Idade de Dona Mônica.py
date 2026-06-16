M = int(input())
A = int(input())
B = int(input())
C = M - (A + B)
if (40 <= M <= 110 and 1 <= A < M and A != B):
    if (A > B and A > C):
        print(A)
    elif (C > A and C > B):
        print(C)
    else:
        print(B)