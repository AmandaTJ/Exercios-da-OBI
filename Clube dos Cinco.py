N = int(input())
a, b, c, d, e, f, g = map(int, input().split())
abc = a + b + c - d - e - f + g
if (abc > N):
    print("S")
else:
    print("N")
    
# A pessoas do tiro com arco
# B pessoas do badminton
# C pessoas da canoagem

# D pessoas do tiro e badminton
# E pessoas do tiro e canoagem
# F pessoas badminton e canoagem
# G nenhum esporte
