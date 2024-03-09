def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    for i in range(len(grid[0])):
        min = 'a'
        for j in range(len(grid)):
            if min > grid[j][i]:
                return "NO"
            else :
                min = grid[j][i]
    return "YES"
