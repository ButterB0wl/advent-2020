file = open('../inputs/day9', 'r')
number_list = file.readlines()

typed_list = list()
for number in number_list:
    typed_list.append(int(number))

preamble = typed_list[:25]
test_list = typed_list[25:]

target = test_list[0]
for target in test_list:
    print(target)
    for i, number in enumerate(preamble[:-1]):
        complement = target - number
        if complement in preamble[i+1:]:
            print(number, complement)
            preamble = preamble[1:]
            preamble.append(target)
            break
    else:
        print('no sln', target)
        invalid_num = target
        break

# day2

index = typed_list.index(invalid_num)
target_list = typed_list[:index]

left_index = 0
right_index = 1

while right_index < len(target_list):
    cont_set = target_list[left_index:right_index+1]
    cont_sum = sum(cont_set)
    if cont_sum < invalid_num:
        right_index += 1
    elif cont_sum > invalid_num:
        left_index += 1
    else:
        print('Contiguous set:', cont_set)
        print('Contiguous sum:', cont_sum)
        print('Encryption Weakness:', min(cont_set) + max(cont_set))
        break
