with open('adventofcode_day8.txt') as file:
    braindead = file.read().splitlines()

code_and_action = []
for item in braindead:
    code_and_action.append(item.split())
#use a flag to determine whether a loop has occured
flag = [False for i in range(len(code_and_action))]

accumulator = 0
index = 0

#Part 1
def traverse(index, accumulator):
    while not flag[index]:
        flag[index] = True
        if code_and_action[index][0] == 'acc':
            accumulator += int(code_and_action[index][1])
            index += 1
        elif code_and_action[index][0] == 'jmp':
            index += int(code_and_action[index][1])
        elif code_and_action[index][0] == 'nop':
            index+=1
    return accumulator

print('Part 1: ', traverse(index, accumulator))



#Part 2
i = len(code_and_action)

#This function is called each time we make a change to 'jmp' or 'nop'
#It is the same code as traverse() for traversing the opcode from start to finish, but with a check to see whether the last opcode is being reached successfully.
def traverse_part_2(index, accumulator, flag):
    limit = len(code_and_action)
    index = 0
    try:
        while not flag[index]:
            flag[index] = True
            if code_and_action[index][0] == 'acc':
                accumulator += int(code_and_action[index][1])
                index += 1
            elif code_and_action[index][0] == 'jmp':
                index += int(code_and_action[index][1])
            elif code_and_action[index][0] == 'nop':
                index+=1
    except:
        pass
    if index != limit:
        return False
    elif index == limit:
        print('Achieved!')
        return accumulator

#We traverse the opcode line by line looking for a 'jmp' or 'nop'
#We make a change to 'nop' or 'jmp' and call the traverse_part2 function to see whether the last line of opcode is being reached. 
#If it doesnt, we reset the current'jmp' or 'nop' value,  move on to the next 'jmp/nop' in the opcode and call traverse once more

def switch_one_line(current_code, substitute):

    x = 0
    index = 0
    flag = [False for i in range(len(code_and_action))]
    
    while x < i:
        output_achieved = False
        if code_and_action[x][0] == current_code:
            code_and_action[x][0] = substitute

            answer = traverse_part_2(index, accumulator, flag)

            if answer is False:
                code_and_action[x][0] = current_code
                flag = [False for i in range(len(code_and_action))]
                x+=1
            else:
                print('Yay')
                output_achieved = True
                x = i+1
                return answer
        else:
            x+=1
    return -1

output = switch_one_line('nop','jmp')

if output == -1:
   output = switch_one_line('jmp', 'nop')
   print("Part 2: ", output)
else:
    print("Part 2: ", output)
