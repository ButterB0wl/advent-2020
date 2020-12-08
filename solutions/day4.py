file = open('../inputs/day4', 'r')
passports = file.readlines()
passport_list = list()
passport = list()
required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

for line in passports:
    if line == '\n' or line == passports[-1]:
        print(passport)
        passport_list.append(passport)
        passport = list()
        continue
    passport = passport + line.strip().split(' ')
    
valid_passports = 0
for passport in passport_list:
    fields_present = dict()
    for field in passport:
        fields_present[field.split(':')[0]] = field.split(':')[1]
    if not required_fields.issubset(fields_present.keys()):
        continue
    if not (1920 <= int(fields_present['byr']) <= 2002 and len(fields_present['byr']) == 4):
        continue
    if not (2010 <= int(fields_present['iyr']) <= 2020 and len(fields_present['iyr']) == 4):
        continue
    if not (2020 <= int(fields_present['eyr']) <= 2030 and len(fields_present['eyr']) == 4):
        continue
    if not ('cm' or 'in' in fields_present['hgt']):
        continue
    if 'cm' in fields_present['hgt'] and not 150 <= int(fields_present['hgt'][:-2]) <= 193:
        continue
    if 'in' in fields_present['hgt'] and not 59 <= int(fields_present['hgt'][:-2]) <= 76:
        continue
    if not (fields_present['hcl'][0] == '#' and len(fields_present['hcl']) == 7):
        continue
    try:
        for letter in fields_present['hcl'][1:]:
            if letter.isdigit() and not 0 <= int(letter) <= 9:
                break
            if letter.isalpha() and not letter in set(['a', 'b', 'c', 'd', 'e', 'f']):
                break
    except StopIteration:
        continue
    if fields_present['ecl'] not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        continue
    if not (fields_present['pid'].isdigit() and len(fields_present['pid']) == 9):
        continue
    
    print(fields_present)
    valid_passports += 1

print(valid_passports)

