seq = list(map(int, input().split()))
seq.sort(key=lambda x: -x)
print(*seq)
