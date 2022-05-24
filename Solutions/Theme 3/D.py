n = int(input())
seq = list()
for _ in range(n):
    seq.append(list(map(int, input().split())))
seq.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
for i in range(n):
    print(*seq[i])
