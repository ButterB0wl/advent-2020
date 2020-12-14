file = open('../inputs/day6', 'r')
forms = file.readlines()

group_counts = list()

yes_list = set()
for form in forms:
    if form == '\n' or form == forms[-1]:
        print(yes_list)
        group_counts.append(len(yes_list))
        yes_list = set()
    else:
        form = form.strip('\n')
        for question in form:
            yes_list.add(question)

print(group_counts)
print(sum(group_counts))

# part 2

group_counts = list()
group_forms = list()
for form in forms:
    if form == '\n' or form == forms[-1]:
        common_yes = set(group_forms[0]).intersection(*group_forms)
        print(common_yes)
        group_counts.append(len(common_yes))
        group_forms = list()
    else:
        form = form.strip('\n')
        group_forms.append(form)

print(group_counts)
print(sum(group_counts))
