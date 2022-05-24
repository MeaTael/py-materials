n = int(input())
mp = dict()
for _ in range(n):
    [name, mark] = input().split()
    if name in mp:
        mp[name][0] += int(mark)
        mp[name][1] += 1
    else:
        mp[name] = [int(mark), 1]
    print(mp[name][0] // mp[name][1])
