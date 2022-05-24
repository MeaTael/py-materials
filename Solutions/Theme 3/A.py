seq = list(map(int, input().split()))
count = 0
for num in seq:
    if num < 0:
        count += 1
print(count)
