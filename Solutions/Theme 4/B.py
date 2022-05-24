seq = list(map(int, input().split()))
mp = dict()
for i in range(len(seq)):
    if seq[i] in mp:
        print("YES")
    else:
        mp[seq[i]] = None
        print("NO")
