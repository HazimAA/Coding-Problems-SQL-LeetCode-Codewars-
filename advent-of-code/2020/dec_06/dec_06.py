with open('adventofcode_day6.txt') as file:
    sp = file.read().split('\n\n')

answers_from_groups = [group.replace('\n','') for group in sp]
unique_answers_for_each_group = [''.join(set(answers)) for answers in answers_from_groups]
count = sum(len(answer) for answer in unique_answers_for_each_group)
print('Part 1: ', count)

s = 0
for line in sp:
    ans = [set(x) for x in line.split()]
    s += len(set.intersection(*ans))

print("Part 2: ", s)
