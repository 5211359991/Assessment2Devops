import csv

def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split(','))

    return data

# def read_csv(csvfilename):
#     rows = []
#     with open(csvfilename, 'r') as f:
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#             rows.append(row)
#     return rows

def remove_duplicate_UID(array):
    all_ID = []
    array_duplicates_removed =[]

    for i in range(len(array)): 
        loop_test = (array[i][0])
        if loop_test not in all_ID:
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

def write_csv(array):
    with open('./clean_results.csv', 'w' , newline = "") as f:
        writer = csv.writer(f, delimiter=',')
        #writer.writerow(write_what)
        for i in range(len(array)): 
           writer.writerow(array[i])


def print_to_command(csvfilename):
    array = get_input(csvfilename)
    for i in range(len(array)): 
           print(*(array[i]))