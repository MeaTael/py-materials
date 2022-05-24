s = list(map(int, input().split()))
num, eq = 0, 0
for k in range(0, len(s)):
    p = s.count(s[k])
    if p > eq:
        num = s[k]
        eq = p
print(num)
