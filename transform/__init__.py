def remove_duplicate_UID(array):
    all_ID = []
    array_duplicates_removed =[]

    for i in range(len(array)): 
        loop_test = (array[i][0])
        ifd loop_test not in all_ID:
            array_duplicates_removed.append(array[i])
        all_ID.append(loop_test)

    return(array_duplicates_removed)

def remove_empty_lines(array):
    empty_lines_removed =[]

    for i in range(len(array)): 
        loop_test = (array[i])
        whole_line = ""
        
        for j in range(len(loop_test)):
            whole_line = whole_line + array[i][j]
        if whole_line != "":
            empty_lines_removed.append(array[i])

    return(empty_lines_removed)


def Capitalize_Array(array):

    for i in range(1,len(array)): 
        array[i][1] = (array[i][1]).capitalize()
        array[i][2] = (array[i][2]).capitalize()

    return(array)

def Validate_Q3(array):
    Q3_invalid_lines_removed = [array[0]]

    for i in range(1,len(array)): 
        Q3 = int(array[i][5])
        if 0 < Q3 < 11:
            Q3_invalid_lines_removed.append(array[i])

    return(Q3_invalid_lines_removed)