n = int(input())
mp = dict()
for i in range(n):
    k = int(input())
    for _ in range(k):
        [name, mark] = input().split()
        if name not in mp:
            mp[name] = [0 for _ in range(n)]
        mp[name][i] = int(mark)
for key in sorted(mp.keys()):
    print(key, *mp[key], sep='\t')
