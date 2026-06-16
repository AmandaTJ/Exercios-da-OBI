X = int(input()) # quota mensal

if 1 <= X <= 100:

    N = int(input()) #numero de meses

    if 1 <= N <= 100:

        tem = X #o que ele tem 

        for i in range(N):
            uso = int(input()) #o que ele usou nesses meses

            if 0 <= uso <= internet:
                internet = internet - uso + X # a quantidade que ele vai poder usar no proximo mes

        print(internet)