import csv
from extract import get_input

def write_csv(array):
    with open('./clean_results.csv', 'w' , newline = "") as f:
        writer = csv.writer(f, delimiter=',')
        #writer.writerow(write_what)
        for i in range(len(array)): 
           writer.writerow(array[i])


def print_to_command(array):
    # array = get_input(csvfilename)
    for i in range(len(array)):
           print(*(array[i]))