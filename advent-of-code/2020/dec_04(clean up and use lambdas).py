with open('adventofcode_day4.txt') as file:
    sp = file.read()
    # print(sp)

passport_count = 0
#We get each passport entry as lines
lines = sp.split("\n\n")
#We get each line in the passport entry text
for line in lines:
    sublines = line.split("\n")
    parameter_count = 0
    cid_flag = 0
    #We split the verious key-pair values into separate lines
    for subline in sublines:
        key_value = subline.split(" ")
        # print("inner iteration")
        #We now work on counting the key values in each passport.
        for pair in key_value:
            parts = pair.split(":")
            try:
                print("key:[{0}], value:[{1}]".format(parts[0], parts[1]))
                #DATA VALIDATION SECTION
                # parameter_count+=1
                #ALLOW CID TO BE A MISSING FIELD


                if parts[0] == 'byr':
                    if int(parts[1]) >=1920 and int(parts[1]) <=2002:
                        parameter_count+=1
                if parts[0] == 'iyr':
                    if int(parts[1]) >= 2010 and int(parts[1]) <=2020:
                        parameter_count+=1
                if parts[0] == 'eyr':
                    if int(parts[1]) >=2020 and int(parts[1]) <= 2030:
                        parameter_count+=1
                if parts[0] == 'hgt':
                    num = parts[1]
                    try:
                        x = int(num[:-2])
                    except:
                        pass
                    print(x)
                    if parts[1].endswith('cm'):
                        if x >=150 and x <= 193:
                            parameter_count+=1
                    elif parts[1].endswith('in'):
                        if x >= 59 and x <=76:
                            parameter_count+=1
                    else:
                        pass
                if parts[0] == 'hcl':
                    if len(parts[1]) == 7 and all(c.isdigit() or c in 'abcdef#' for c in parts[1]):
                        parameter_count+=1
                if parts[0] == 'ecl':
                    if parts[1] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                        parameter_count+=1
                if parts[0] == 'pid':
                    if len(parts[1]) == 9 and all(c.isdigit() for c in parts[1]):
                        parameter_count+=1
                if parts[0] == 'cid':
                    cid_flag = 1
                    parameter_count+=1
            except:
                print(f"You have reached the end of the file.")
            print(parameter_count)
    if parameter_count == 8:
        passport_count += 1
    elif parameter_count == 7 and cid_flag == 0:
        passport_count += 1
    print(parameter_count, cid_flag, passport_count)

print(passport_count)
