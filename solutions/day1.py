file = open('../inputs/day1', 'r')
expenses = file.readlines()
expenses = [int(i) for i in expenses]

for i in expenses:
    for j in expenses:
        if i == j:
            continue
        if i + j == 2020:
            print(i * j)
            break

for i in expenses:
    for j in expenses:
        if i == j:
            continue
        for k in expenses:
            if i == k or j == k:
                continue
            if i + k + j == 2020:
                print(i * j * k)
                break