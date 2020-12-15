file = open('../inputs/day8', 'r')
instructions = file.readlines()

instruction_list = list()
visited_list = dict()
for instruction in instructions:
    instruction = instruction.strip('\n').split(' ')
    instruction_list.append(tuple((instruction[0], int(instruction[1]))))
    visited_list[len(instruction_list)-1] = False
# print(instruction_list)
# print(visited_list)

def execute(index: int, acc: int):
    next_index = index
    print(instruction_list[index])
    if instruction_list[index][0] == 'acc':
        acc += instruction_list[index][1]
        next_index += 1
    elif instruction_list[index][0] == 'jmp':
        next_index += instruction_list[index][1]
    else:
        next_index += 1
    visited_list[index] = True
    return next_index, acc

index = 0
acc = 0
while not visited_list[index]:
    index, acc = execute(index, acc)

print(acc)

