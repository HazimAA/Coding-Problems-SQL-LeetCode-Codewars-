#ADVENT OF CODE DAY 5
## This code was written before I realised the problem could be solved by converting to binary

with open('adventofcode_day5.txt') as file:
    entries = file.read().splitlines()

final = []

def row_and_col(total, lower, upper, b_or_f):
    row_val = 0
    if (b_or_f == 'F') or (b_or_f == 'L'):
        upper = upper - math.floor(total/2) - 1
    elif (b_or_f == 'B') or (b_or_f == 'R'):
        lower = lower + math.ceil(total/2)
    total = upper - lower
    row_val = lower
    return total, lower, upper, row_val

def find_my_seat(list):
    return [x for x in range(list[0], list[-1]+1) if x not in list]

for entry in entries:
    i,j = 0,7
    row_total, col_total = 127, 7
    row_upper, col_upper = 127, 7
    row_lower, col_lower = 0, 0

    for i in range(0,7,1):
        row_total, row_lower, row_upper, row_val = row_and_col(row_total, row_lower, row_upper, entry[i])
        i+=1

    for j in range(7,10):
        col_total, col_lower, col_upper, col_val = row_and_col(col_total, col_lower, col_upper, entry[j])
        j+=1
    
    x = (row_val * 8) + col_val
    final.append(x)

sorted_seats = sorted(final)
print("Part 1: The highest seat Id is: ",max(final))
print("Part 2: My seat is:", find_my_seat(sorted_seats))
