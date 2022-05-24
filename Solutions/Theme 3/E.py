[m, n, k] = list(map(int, input().split()))
field = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    [x, y] = list(map(int, input().split()))
    field[x-1][y-1] = "*"
d_x = [0, 0, 1, -1]
d_y = [1, -1, 0, 0]
for i in range(m):
    for j in range(n):
        for p in range(4):
            if field[i][j] != "*" and 0 <= i+d_y[p] < m and 0 <= j+d_x[p] < n:
                if field[i+d_y[p]][j+d_x[p]] == "*":
                    field[i][j] += 1
for i in range(m):
    print(*field[i])
