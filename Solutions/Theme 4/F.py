file = open("input.txt", "r")
data = file.read()
file.close()
mp = dict()
mx = 0
for char in data:
    if char != ' ' and char != '\n':
        if char in mp:
            mp[char] += 1
        else:
            mp[char] = 1
        if mp[char] > mx:
            mx = mp[char]
for i in range(mx):
    for key in sorted(mp.keys()):
        if mp[key] == mx:
            print("#", end='')
            mp[key] -= 1
        else:
            print(' ', end='')
    mx -= 1
    print()
print(''.join(sorted(mp.keys())))
