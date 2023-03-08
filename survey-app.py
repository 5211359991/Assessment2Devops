import csv
from extract import get_input, remove_duplicate_UID,remove_empty_lines,Capitalize_Array,Validate_Q3,write_csv,print_to_command


def input(csvfilename):
    array = get_input(csvfilename)
    array = remove_duplicate_UID(array)
    array = remove_empty_lines(array)
    array = Capitalize_Array(array)
    array = Validate_Q3(array)
    write_csv(array)
    return(array)


input('./results.csv')
print_to_command('./clean_results.csv')