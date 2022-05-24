seq = list(map(int, input().split()))
mp = dict()
for num in seq:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1
for key in sorted(mp.keys()):
    print(key, mp[key])
