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
        break
