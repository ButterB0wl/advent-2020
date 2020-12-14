file = open('../inputs/day6', 'r')
forms = file.readlines()

group_counts = list()

yes_list = set()
for form in forms:
    if form == '\n':
        print(yes_list)
        group_counts.append(len(yes_list))
        yes_list = set()
    else:
        form = form.strip('\n')
        for question in form:
            yes_list.add(question)

print(yes_list)
group_counts.append(len(yes_list))

print(group_counts)
print(sum(group_counts))