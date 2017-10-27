#Starting in the top left corner of a 2×2 grid,
#and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

n = 20
paths = [[1 for i in range(n)] for j in range(n)]

for i in range(1, n):
    for j in range(1, n):
        paths[i][j] = paths[i-1][j] + paths[i][j-1]

total = sum(sum(x) for x in paths) + 1

print (total)
