import math
[A, B, C] = list(map(int, input().split()))
if a == 0 and b == 0 and c == 0:
    print("ANY")
elif a == 0 and b == 0 and c != 0:
    print("NO SOLUTIONS!")
elif a == 0:
    print(-C / B)
else:
    D = B ** 2 - 4 * A * C
    if D < 0:
        print("NO SOLUTIONS")
    elif D == 0:
        print(-B / (2 * A))
    else:
        print((-B + math.sqrt(D) / (2 * A)), end=" ")
        print((-B - math.sqrt(D) / (2 * A)))
