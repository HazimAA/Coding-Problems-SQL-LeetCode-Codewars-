with open('adventofcode_day9.txt') as file:
    contents = file.read().splitlines()

what_do_the_numbers_mean_mason = [int(num) for num in contents]
preamble_length = 25
flags = []

## ************************** Part 1 **********************************

for i in range(preamble_length, len(what_do_the_numbers_mean_mason),1):
    current_value = what_do_the_numbers_mean_mason[i]
    past_values = what_do_the_numbers_mean_mason[i - preamble_length : i]
    for x in past_values:
        if (current_value - x)  not in past_values:
            flags.append(False)
        else:
            flags.append(True)
    if any(flags) is False:
        output = current_value
    flags = []

print('Part 1: ', output)

## **************************** Part 2 *******************************

#awesome way to do subset sum, but only returns one answer. so will work only if one solution exists.
for index, num in enumerate(what_do_the_numbers_mean_mason):
    #num is the starting value, we keep adding consecutive numbers from this starting value, until the sum exceeds required value
    #if sum exceeds required value, the starting position is incremented and we start calculating the sum once more.
    values = []
    running_sum = 0
    idx = index
    #code for calculating the sum of consecutive numbers from starting position
    while running_sum < output:
        running_sum += what_do_the_numbers_mean_mason[idx]
        values.append(what_do_the_numbers_mean_mason[idx])
        idx += 1

    if running_sum == output:
        print("Part 2: ", max(values) + min(values))
        print(values)
        break
