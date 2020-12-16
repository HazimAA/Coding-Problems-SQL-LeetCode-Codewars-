with open('adventofcode_day12.txt')as file:
    travel_log = file.read().splitlines()

instructions = [[l.strip()[0], int(l.strip()[1:])] for l in open('adventofcode_day12.txt', 'r')]
print(instructions)

facing = {"N":0,"S":0,"E":0,"W":0}
waypoint = {"N":1,"S":0,"E":10,"W":0}

directions = "NESW"
current_direction = directions[1]

def change_the_direction(turn, angle):
    if turn == "R":
        value = angle//90
    elif turn  == "L":
        value = -angle//90
    return value

# PART 1
for instr in instructions:
    if instr[0] == "L" or instr[0] == "R":
        current_direction = directions[(directions.find(current_direction) + change_the_direction(instr[0], instr[1]))%4]
    elif instr[0] == "F":
        facing[current_direction]+=instr[1]
    else:
        facing[instr[0]] += instr[1]

print("PART 1: ",abs(facing["N"] - facing["S"]) + abs(facing["E"] - facing["W"]))



#PART 2

facing = {"N":0,"S":0,"E":0,"W":0}
waypoint = {"N":1,"S":0,"E":10,"W":0}

directions = "NESW"
current_direction = directions[1]
waypoint_direction = directions[0]
trial_waypoint = [10,1]

def change_the_direction(turn, angle, current_direction, waypoint_direction):
    temporary_value_of_old_direction = waypoint[current_direction]
    temporary_value_of_old_waypoint_direction = waypoint[waypoint_direction]
    if turn == "R":
        value = angle//90
    elif turn  == "L":
        value = -angle//90
    return value, temporary_value_of_old_direction, temporary_value_of_old_waypoint_direction

for instr in instructions:
    if instr[0] == "L" or instr[0] == "R":
        if instr[0] == "R":
            value_for_cal, old_direction_value, old_waypoint_value = change_the_direction(instr[0],instr[1],current_direction,waypoint_direction)
            temp_waypoint_direction = waypoint_direction
            waypoint_direction = directions[(directions.find(current_direction) + value_for_cal)%4]
            current_direction = directions[(directions.find(temp_waypoint_direction) + value_for_cal)%4]
            if instr[1] == 270:
                loc_one = -trial_waypoint[1]
                loc_zero = trial_waypoint[0]
                trial_waypoint[0] = loc_one
                trial_waypoint[1] = loc_zero
            elif instr[1] == 180:
                loc_one = -trial_waypoint[0]
                loc_zero = -trial_waypoint[1]
                trial_waypoint[0] = loc_one
                trial_waypoint[1] = loc_zero
                z = waypoint_direction
                waypoint_direction = current_direction
                current_direction = z
            else:
                loc_one = trial_waypoint[1]
                loc_zero = -trial_waypoint[0]
                trial_waypoint[0] = loc_one
                trial_waypoint[1] = loc_zero

        if instr[0] == "L":
            value_for_cal, old_direction_value, old_waypoint_value = change_the_direction(instr[0],instr[1],current_direction,waypoint_direction)
            temp_waypoint_direction = waypoint_direction
            waypoint_direction = directions[(directions.find(current_direction) + value_for_cal)%4]
            current_direction = directions[(directions.find(temp_waypoint_direction) + value_for_cal)%4]

            if instr[1] == 180:
                loc_one = -trial_waypoint[0]
                loc_zero = -trial_waypoint[1]
                trial_waypoint[0] = loc_one
                trial_waypoint[1] = loc_zero
                z = waypoint_direction
                waypoint_direction = current_direction
                current_direction = z
            elif instr[1] == 270:
                loc_one = trial_waypoint[1]
                loc_zero = -trial_waypoint[0]
                trial_waypoint[0] = loc_one
                trial_waypoint[1] = loc_zero
            else:
                loc_one = -trial_waypoint[1]
                loc_zero = trial_waypoint [0]
                trial_waypoint[0] = loc_one
                trial_waypoint[1] = loc_zero
    #moves ship to waypoint certain amount of times
    elif instr[0] == "F":
        opp_of_current = directions[(directions.find(current_direction) + 2) % 4]
        opp_of_waypoint = directions[(directions.find(waypoint_direction) + 2) % 4]
        facing[current_direction] += trial_waypoint[0] * instr[1]
        facing[waypoint_direction] += trial_waypoint[1] * instr[1]
    #moves the waypoint, ship remains where it is
    else:
        if instr[0] == "N":
            trial_waypoint[1] += instr[1]
        if instr[0] == "S":
            trial_waypoint[1] -= instr[1]
        if instr[0] == "E":
            trial_waypoint[0] += instr[1]
        if instr[0] == "W":
            trial_waypoint[0] -= instr[1]

print("PART 2: ",abs(facing["N"] + facing["S"]) + abs(facing["E"] + facing["W"]))
print("")
