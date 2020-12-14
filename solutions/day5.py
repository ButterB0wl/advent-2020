file = open('../inputs/day5', 'r')
passes = file.readlines()

def split_list(indices: list, left: bool) -> list:
    half = len(indices)//2
    if left:
        return indices[:half]
    else:
        return indices[half:]

seat_ids = list()

for p in passes:
    rows = list(range(0, 128))
    cols = list(range(0, 8))

    row_parts = p[:7]
    col_parts = p[7:]
    print(row_parts, col_parts)

    for part in row_parts:
        if part == 'F':
            rows = split_list(rows, True)
        else:
            rows = split_list(rows, False)
        print(rows)

    for part in col_parts:
        if part == 'L':
            cols = split_list(cols, True)
        else:
            cols = split_list(cols, False)
        print(cols)
    
    id = rows[0] * 8 + cols[0]
    seat_ids.append(id)

print(max(seat_ids))

