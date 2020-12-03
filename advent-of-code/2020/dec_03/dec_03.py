def count_of_trees_encountered(input, right, down):
    #rearrange the entries to get the requisite 32 rows
    input = np.array(input_array).reshape(-1,32)
    #deletes the empty '' which is present as the last element in each sublist
    final = np.delete(input,-1,1)
    copy = final

    #Current Count of Rows and Columns. Only Columns will increase as the Program executes.
    rows, columns = final.shape
    curr_row, curr_col = 0, 0
    trees = 0
    # final = np.hstack((final, copy))

    while curr_row < rows:
        #Traverse the slope, Right 3, Down 1
        curr_row+=down
        curr_col+=right
        #Try - Catch in case Row count is exceeded.
        try:
            # if tree spotted
            if final[curr_row,curr_col] == '#':
                trees+=1
        except:
            return trees
        #if end of column reached, or within reach then stackkkkk
        if curr_col >= columns-right:
            #Add another copy of the Input array laterally
            final = np.hstack((final,copy))
            rows, columns = final.shape

    return trees

with open('adventofcode_day3.txt') as file:
    #loads each element as entry in numpy array
    input_array = np.array([element.strip('\n') for line in file for element in line])

Trees = count_of_trees_encountered(input_array,1,1) * count_of_trees_encountered(input_array,3,1) * count_of_trees_encountered(input_array,5,1) * count_of_trees_encountered(input_array, 7, 1) * count_of_trees_encountered(input_array, 1, 2)
print(Trees)
