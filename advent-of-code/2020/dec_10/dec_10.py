with open('adventofcode_day10.txt') as file:
    contents = file.read().splitlines()

joltages = [int(num) for num in contents]
joltages.append(0)
joltages.append(max(joltages)+3)
ordered_joltages = sorted(joltages)

elements = len(ordered_joltages) - 1
start = 0
diff_of_1 = 0
diff_of_3 = 0

while start < elements:
    if (ordered_joltages[start] + 1) == ordered_joltages[start+1]:
        diff_of_1+=1
        start += 1
    elif (ordered_joltages[start] + 2) == ordered_joltages[start + 1]:
        start += 1
    else:
        diff_of_3 += 1
        start +=1
print("Part 1: ", diff_of_1 * diff_of_3)


#PART 2

sol = {}
for line in ordered_joltages:
    sol[line] = 0
    if line - 1 in sol:
        sol[line]+=sol[line-1]
    if line - 2 in sol:
        sol[line]+=sol[line-2]
    if line - 3 in sol:
        sol[line]+=sol[line-3]
    if line ==0:
        sol[line] = 1

print("PART 2: ", sol[max(ordered_joltages)])
