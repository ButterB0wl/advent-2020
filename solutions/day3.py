file = open('../inputs/day3', 'r')
forest = list(map(lambda row: row.strip(), file.readlines()))
right_index = len(forest[0])-1
bottom_index = len(forest)-1

x = y = 0
tree_count = 0

while y <= bottom_index:
    if x > right_index:
        x = x - (right_index + 1)

    if forest[y][x] == '#':
        tree_count += 1
    x += 3
    y += 1

print(tree_count)
