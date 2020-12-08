file = open('../inputs/day3', 'r')
forest = list(map(lambda row: row.strip(), file.readlines()))
right_index = len(forest[0])-1
bottom_index = len(forest)-1

def tree_counter(x_move, y_move):
    x = y = 0
    tree_count = 0
    while y <= bottom_index:
        if x > right_index:
            x = x - (right_index + 1)

        if forest[y][x] == '#':
            tree_count += 1
        x += x_move
        y += y_move
    return tree_count

print(tree_counter(1, 1))
print(tree_counter(3, 1))
print(tree_counter(5, 1))
print(tree_counter(7, 1))
print(tree_counter(1, 2))

tree_product = tree_counter(1, 1)
tree_product *= tree_counter(3, 1)
tree_product *= tree_counter(5, 1)
tree_product *= tree_counter(7, 1)
tree_product *= tree_counter(1, 2)

print(tree_product)
