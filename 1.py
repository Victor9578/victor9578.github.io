n = 3
matrix = [[0] * n for _ in range(n)]
a = [[0]*4]
print(a)
a[0][3] = 1
print(a)
print(id(a[0][1]))
print(id(a[0][2]))
print(id(a[0][3]))
print(id(a[0][0]))
# x, y = 0, 0
# res = []
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# di = 0
# visited = set()
# m, n = len(matrix), len(matrix[0])

# for i in range(1, m * n + 1):
#     print(x, y)
#     matrix[x][y] = i
#     print(matrix)
#     visited.add((x, y))
#     tx, ty = x + dx[di], y + dy[di]
#     if 0 <= tx < m and 0 <= ty < n and (tx, ty) not in visited:
#         x, y = tx, ty
#     else:
#         di = (di + 1) % 4
#         x, y = x + dx[di], y + dy[di]
# return matrix
