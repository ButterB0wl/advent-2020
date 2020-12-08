file = open('../inputs/day2', 'r')
passwords = file.readlines()
print(passwords)

num_valid = 0
num_valid_2 = 0
for p in passwords:
    p = p.strip('\n').split(':')
    rule = p[0]
    pw = p[1]
    rule = rule.split(' ')
    range = rule[0]
    letter = rule[1]
    range = range.split('-')
    low = int(range[0])
    high = int(range[1])
    count = pw.count(letter)
    if count >= low and count <= high:
        num_valid += 1
        print(count, low, high)
    if pw[low] == letter or pw[high] == letter:
        print(pw, pw[low], pw[high])
        if pw[low] == letter and pw[high] == letter:
            continue
        else:
            num_valid_2 += 1
    
print(num_valid)
print(num_valid_2)