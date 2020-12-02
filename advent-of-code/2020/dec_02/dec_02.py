def part_one(password_list):
    #We will assign a password one by one to the variable individual entry, and work on this variable to obtain our result
    i=0
    valid_password_count = 0
    
    while i < 1000:
        #Each entry is split into three sections: 'numbers', 'the letter to be searched', and 'the password' sections
        individual_entry = password_list[i].split()

        #We will clean up the letters section first, to isolate just the letter
        # stripping unwanted ':' from the 'letter to be searched section' that will be used to identify letters in the password section
        letter = individual_entry[1].strip(':')
        #We will clean up the numbers section, to isolate just the min and max numbers
        #finding the digits from the 'numbers' section
        min_max = [int(s) for s in individual_entry[0].split('-') if s.isdigit()]
        # print(individual_entry[0].split('-'), min_max)
        #assigning the 'password' section to a variable
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
        #Each entry is split into three sections: 'numbers', 'the letter to be searched', and 'the password' sections
        individual_entry = password_list[i].split()

        #We will clean up the letters section first, to isolate just the letter
        # stripping unwanted ':' from the 'letter to be searched section' that will be used to identify letters in the password section
        letter = individual_entry[1].strip(':')
        #We will clean up the numbers section, to isolate just the min and max numbers
        #finding the digits from the 'numbers' section
        min_max = [int(s) for s in individual_entry[0].split('-') if s.isdigit()]
        min_max[0] = min_max[0] - 1
        min_max[1] = min_max[1] - 1
        # print(individual_entry[0].split('-'), min_max)
        #assigning the 'password' section to a variable
        password = individual_entry[2]

        if (password[min_max[0]] == letter or password[min_max[1]] == letter) and (password[min_max[0]] != password[min_max[1]]):
            valid_password_count+= 1

        i+=1

    return valid_password_count


with open('adventofcode_day2.txt') as file_object:
    password_list = [line.strip('\n') for line in file_object]
    #The password_list has the master copy of all passwords
    print("Part 1 solution: ", part_one(password_list))
    print("Part 2 solution: ", part_two(password_list))
