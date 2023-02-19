# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import os
import sys


def create_filename_out(filename_in):
    filename, file_extension = os.path.splitext(filename_in)
    filename_out = filename + '_out' + file_extension
    return filename_out


def read_file(filename_in):
    with open(filename_in, newline='') as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        filename_out = create_filename_out(filename_in)
        print('Output naar: ' + filename_out)

        f = open(filename_out, "a")

        for row in csvreader:
            for index, field in enumerate(row):
                if index == 0:
                    new_row = row[0]
                else:
                    if index == 11 or index == 17:
                        new_field = ',' + field + ''
                    else:
                        new_field = ',"' + field + '"'
                    new_row += new_field
            f.write(new_row+'\n')

        f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total_arguments_passed = len(sys.argv)
    if total_arguments_passed == 1:
        print('\n===>ERROR: Foute aanroep, je moet de filename meegeven als parameter')
        print()
        exit()
    filename_in = sys.argv[1]
    run_dir = os.getcwd()
    filepath_in = os.path.join(run_dir, filename_in)

    read_file(filepath_in)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
