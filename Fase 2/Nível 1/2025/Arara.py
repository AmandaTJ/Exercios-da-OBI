n, m = map(int, input().split())
gaiolas = 1 + 5 * (n - 1)

if gaiolas <= m:
    print("S")
else:
    print("N")