import csv
from extract import get_input 
#from transform import remove_duplicate_UID,remove_empty_lines,Capitalize_Array,Validate_Q3
from output import write_csv,print_to_command

#def input(csvfilename):
#    array = get_input(csvfilename)
   # array = remove_duplicate_UID(array)
 #   array = remove_empty_lines(array)
  #  array = Capitalize_Array(array)
   # array = Validate_Q3(array)
    #write_csv(array)
    #print_to_command("./clean_results.csv")
    #return(array)


#print(input("./results.csv"))

print('hello')

import csv

#def read_csv_file(file_name):
    #data = []
    #with open(file_name, 'r') as file:
        #reader = csv.reader('results.csv')
        #for row in reader:
            #data.append(row)
    #return data

def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip().split(','))
    return data

print(get_input('results.csv'))
data = (get_input('results.csv'))

# remove duplicates

def remove_duplicates(data):
    unique_ids = {}
    array_duplicates_removed = []

    for row in data:
        user_id = row[0] #assuming user ID is in the first column
        if user_id not in unique_ids:
            unique_ids[user_id] = True
            array_duplicates_removed.append(row)

    return array_duplicates_removed        

array_duplicates_removed = remove_duplicates(data)
data = remove_duplicates(data)

print(data)

#remove empty lines (array)

#def remove_empty_lines(data):
    #array_without_empty_lines = [row for row in data if row] #rewrite - how to remove empty lines from list
    #return array_without_empty_lines
            
#data = remove_empty_lines(data)
#print(data)

#def get_input(filename):

    #data = []

    #with open(filename, 'r') as f:

        #for line in f.readlines():

            #data.append(line.strip().split(','))




    #return data


 #  array = Capitalize_Array(array)

def capitalize_names(data):
    capitalized_data = []

    for row in data:
        capitalized_row = [name.capitalize() if index in [1, 2] else name for index, name in enumerate(row)]
        capitalized_data.append(capitalized_row)

    return capitalized_data

capitalized_data = capitalize_names(data)
data = capitalize_names(data)
print(data)

# array = Validate_Q3(array)

#def validate_answer3(data):
    #valid_data = []

    #for row in data:
        #if len(row) >= 3 and row[2].isdigit():
            #answer3 = int(row[2])
            #if 1 <= answer3 <= 10:
                #valid_data.append(row)

    #return valid_data    

#valid_data = validate_answer3(data)
#data = validate_answer3(data)
#print(data)

#def Validate_Q3(array): (CSE)

    #Q3_invalid_lines_removed = [array[0]] (CSE)




   # for i in range(1,len(array)):

        #Q3 = int(array[i][5])

        #if 0 < Q3 < 11:

            #Q3_invalid_lines_removed.append(array[i]) (CSE, make sure the same)




    #return(Q3_invalid_lines_removed) (CSE, make sure the same)

       #write_csv(array)

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

#assuming valid_data contains the clenased data

save_to_csv(data, 'clean_results.csv')


#create an output script

def print_to_command(csvfilename):
    array = get_input(csvfilename)
    for i in range(len(array)):
       print(*(array[i]))

print_to_command('clean_results.csv')

