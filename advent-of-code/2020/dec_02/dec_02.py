def part_one(password_list):
    i=0
    valid_password_count = 0
    
    while i < 1000:
        individual_entry = password_list[i].split()
        letter = individual_entry[1].strip(':')
        min_max = [int(s) for s in individual_entry[0].split('-') if s.isdigit()]
        password = individual_entry[2]

        if password.count(letter) >= min_max[0] and password.count(letter) <= min_max[1]:
            valid_password_count+=1
        i+=1
    return valid_password_count


def part_two(password_list):
    i = 0
    valid_password_count = 0
    #ADVENT OF CODE DAY 2 - PART 2
    
    while i < 1000:
        individual_entry = password_list[i].split()

        letter = individual_entry[1].strip(':')
        min_max = [int(s) for s in individual_entry[0].split('-') if s.isdigit()]
        min_max[0] = min_max[0] - 1
        min_max[1] = min_max[1] - 1
        password = individual_entry[2]

        if (password[min_max[0]] == letter or password[min_max[1]] == letter) and (password[min_max[0]] != password[min_max[1]]):
            valid_password_count+= 1

        i+=1

    return valid_password_count


with open('adventofcode_day2.txt') as file_object:
    password_list = [line.strip('\n') for line in file_object]
    print("Part 1 solution: ", part_one(password_list))
    print("Part 2 solution: ", part_two(password_list))
