def part_one(input):
    # TO FIND TWO NUMBERS THAT SUM UP TO 2020
    for i, item in enumerate(input):
        for j in range(i + 1, len(input)):
            total_of_two_items = input[i] + input[j]
            if (total_of_two_items == total_number):
                # print('{first_item} {second_item}'.format(first_item=input[i], second_item=input[j]))
                return (input[i] * input[j])


def part_two(input):
    # TO FIND THREE NUMBERS THAT SUM UP TO 2020
    for i, item in enumerate(input):
        for j in range(i + 1, len(input)):
            for k in range(j + 1, len(input)):
                total_of_three_items = input[i] + input[j] + input[k]
                if (total_of_three_items == total_number):
                    # print('{first_item} {second_item} {third_item}'.format(first_item=input[i], second_item=input[j],
                    #                                                        third_item=input[k]))
                    return (input[i] * input[j] * input[k])
                    # print('\n')


with open('adventofcode_day1.txt') as file:
    input = [int(num.rstrip('\n')) for num in file]
    total_number = 2020
    print("Part 1: ", part_one(input))
    print("Part 2: ", part_two(input))
