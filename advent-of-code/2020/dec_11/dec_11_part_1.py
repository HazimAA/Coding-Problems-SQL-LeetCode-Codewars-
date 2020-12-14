def check_unoccupied(i,j):
    flags = []
    if (previous_input_array[i - 1][j] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i][j - 1] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i - 1][j - 1] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i + 1][j] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i][j + 1] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i + 1][j + 1] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i + 1][j - 1] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    if (previous_input_array[i - 1][j + 1] != "#"):
        flags.append(False)
    else:
        flags.append(True)
    # print(flags)
    if any(flags) is False:
        input_array[i][j] = '#'
    flags = []


def check_occupied(i,j):
    count_of_occupied_seats = 0
    flags = []
    if previous_input_array[i - 1][j] == "#":
        flags.append("True")
    if previous_input_array[i][j - 1] == "#":
        flags.append("True")
    if previous_input_array[i - 1][j - 1] == "#":
        flags.append("True")
    if previous_input_array[i + 1][j] == "#":
        flags.append("True")
    if previous_input_array[i,j + 1] == "#":
        flags.append("True")
    if previous_input_array[i + 1][j + 1] == "#":
        flags.append("True")
    if previous_input_array[i + 1][j - 1] == "#":
        flags.append("True")
    if previous_input_array[i - 1][j + 1] == "#":
        flags.append("True")
    for seat in flags:
        if seat == "True":
            count_of_occupied_seats += 1
    if count_of_occupied_seats > 4:
        input_array[i][j] = "L"
    # print(flags,count_of_occupied_seats)
    flags = []
    count_of_occupied_seats = 0



with open('adventofcode_day11.txt') as file:
    input_array = np.array([[char for spots in line.split() for char in spots] for line in file])
    # input_array = [[char for spots in line.split() for char in spots] for line in file]
    # contents = file.read().splitlines()

#padding boundary with '.'
input_array = np.pad(input_array, pad_width=1, mode='constant', constant_values='.')
previous_input_array = input_array.copy()
rows, columns = input_array.shape
i, j = 0, 0
flags = []
occurrences_before = 0
occurrences_after = 1


while occurrences_before != occurrences_after:
    occurrences_before = np.count_nonzero(input_array == "#")
    for i in range(1, rows-1):
        for j in range(1, columns-1):
            if previous_input_array[i,j] == 'L':
                check_unoccupied(i,j)
            elif previous_input_array[i,j] == '#':
                check_occupied(i,j)
            else:
                pass
    previous_input_array = input_array.copy()
    occurrences_after = np.count_nonzero(input_array == "#")

print(input_array)
print(occurrences_after)
