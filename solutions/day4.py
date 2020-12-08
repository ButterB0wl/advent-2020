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
    fields_present = set()
    for field in passport:
        fields_present.add(field.split(':')[0])
    if required_fields.issubset(fields_present):
        print(passport, fields_present)
        valid_passports += 1

print(valid_passports)

