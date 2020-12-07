with open('adventofcode_day7.txt') as file:
    sp = file.read().splitlines()

list_of_bag_and_reqs = [entry.split('contain') for entry in sp]
list_of_potential_parent_bags = ['shiny gold bag']

def find_bags():
    for i in range(0,len(list_of_bag_and_reqs),1):
        #reading the requirements for each bag.
        # print(list_of_bag_and_reqs[i][1])
        requirement = list_of_bag_and_reqs[i][1]
        for bag in list_of_potential_parent_bags:
            if requirement.find(bag) != -1:
                # print(list_of_bag_and_reqs[i][0])
                # print(requirement)
                #Shiny gold bag is used as a primer to find first parent bag
                #we add the parent bag to a list. We then search to see whether the parent bag can be added into another bag as well
                parent_bag_found = list_of_bag_and_reqs[i][0].rstrip('s ')
                if parent_bag_found not in list_of_potential_parent_bags:
                    list_of_potential_parent_bags.append(parent_bag_found)

trial = 0
while len(list_of_potential_parent_bags) != trial:
    trial = len(list_of_potential_parent_bags)
    find_bags()
print('Part 1: ', len(list_of_potential_parent_bags)-1)


def traverse(key, tree):
    # print(key)
    if key == ' no other bags.':
        return 0
    _sum = sum([i for i in tree[key].values()])
    return _sum + sum([tree[key][i] * traverse(i, tree) for i in tree[key]])


tree = {}

for i in range(0,len(list_of_bag_and_reqs),1):
    #reading the requirements for each bag.
    # print(list_of_bag_and_reqs[i][0])
    source_bag = list_of_bag_and_reqs[i][0].rstrip(" ").rstrip('s')
    requirement = list_of_bag_and_reqs[i][1].split(',')
    # print(requirement)
    temp_dict = {}
    for bag in requirement:
        cleaned_up_bag_and_count = bag.replace('.','').rstrip('s').lstrip(' ')
        # print(cleaned_up_bag_and_count)
        split_num_and_text = re.findall(r'[A-Za-z ]+|\d+', cleaned_up_bag_and_count)
        text_and_num = [x.lstrip(' ') for x in split_num_and_text if x]
        # print(text_and_num)
        num = int(text_and_num[0]) if text_and_num[0].isdigit() else 0
        try:
            bag = text_and_num[1]
        except:
            pass
        temp_dict[bag] = num
    tree[source_bag] = temp_dict
# print(tree)

print('Part 2: ', traverse('shiny gold bag', tree))
