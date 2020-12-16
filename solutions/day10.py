file = open('../inputs/day10', 'r')
joltages = file.readlines()

sorted_jolts = list()
for joltage in joltages:
    sorted_jolts.append(int(joltage))

sorted_jolts = sorted(sorted_jolts)
print(sorted_jolts)
ones = 0
threes = 0
for i, jolt in enumerate(sorted_jolts):
    if i == len(sorted_jolts) - 1:
        threes += 1

    else:
        if sorted_jolts[i+1] - sorted_jolts[i] == 3:
            threes += 1
        elif sorted_jolts[i+1] - sorted_jolts[i] == 1:
            ones += 1
        else:
            print('not one or three')

print('Ones: ', ones)
print('Threes: ', threes)

# part 2

def count_arrangements(start_joltage: int, sorted_joltages: list):
    if not sorted_joltages:
        return 1
    arrangements = 0
    print(start_joltage, sorted_joltages)
    for i, joltage in enumerate(sorted_joltages):
        if joltage - start_joltage <= 3:
            if i == 1:
                print('skipped:', sorted_joltages[0])
            if i == 2:
                print('skipped:', sorted_joltages[0], sorted_joltages[1])
            arrangements += count_arrangements(joltage, sorted_joltages[i+1:])
        else:
            break
    return arrangements

arrangements1 = count_arrangements(9, sorted_jolts[5:10])
print(arrangements1)


# print(sorted_jolts)
# print(sorted_jolts[:46])
# print(sorted_jolts[46:])
# print(sorted_jolts[45])
# arrangements1 = count_arrangements(0, sorted_jolts[:46])
# print(arrangements1)
# arrangements2 = count_arrangements(sorted_jolts[45], sorted_jolts[46:])
# print(arrangements2)


