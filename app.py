import csv
from extract import get_input 
from transform import remove_duplicate_UID,remove_empty_lines,Capitalize_Array,Validate_Q3
from output import write_csv,print_to_command

def input(csvfilename):
    array = get_input(csvfilename)
    array = remove_duplicate_UID(array)
    array = remove_empty_lines(array)
    array = Capitalize_Array(array)
    array = Validate_Q3(array)
    #write_csv(array)
    #print_to_command('./clean_results.csv')
    return(array)


a = input('./results.csv')
print_to_command(a)