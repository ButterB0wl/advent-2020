file = open('../inputs/day7', 'r')
rules = file.readlines()

bags = dict()
for rule in rules:
    rule = rule.strip('\n').strip('.').replace(' bags', '').replace(' bag', '').split(' contain ')
    color = rule[0]
    rule = rule[1].split(', ')
    contents = dict()
    for content in rule:
        if content == 'no other':
            break
        contents[content[2:]] = int(content[0])
    bags[color] = contents
    print(color, bags[color])

def find_valid_bags(search_colors: set, all_bags: dict):
    valid_bags = set()
    if not search_colors:
        return valid_bags
    for color, contents in all_bags.items():
        if any(item in search_colors for item in contents):
            valid_bags.add(color)
    return valid_bags.union(find_valid_bags(valid_bags, all_bags))

valid_bags = find_valid_bags('shiny gold', bags)
print(valid_bags)
print(len(valid_bags))




    