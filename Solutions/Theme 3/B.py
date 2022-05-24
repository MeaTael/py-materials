seq = list(map(int, input().split()))
seq[0], seq[1:] = seq[-1], seq[:-1]
print(*seq)
