s = input().split()
for k in range(0, len(s)):
    if s.count(s[k]) == 1:
        print(s[k], end=' ')
