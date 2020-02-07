import csv
import argparse
import sys

def print_file_content(file):
    with open(file) as file_object:
        reader = csv.reader(file_object)

        for row in reader:
            print(str(row))

def write_list_to_file(output_file,lst):
        with open(output_file, 'w') as file_object:
            file_object.write("".join(lst))

def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
        return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads from a file and write to an other file')
    parser.add_argument('path', help='Path to read files from')
    parser.add_argument('-f','--file', help='File to write to')
    args = parser.parse_args()
    print(parser.parse_args())

path_to_file = args.path

if args.file is None:
    print_file_content(path_to_file)
else:
    lines = read_csv(args.path)
    write_list_to_file(args.file,lines)
    print(lines)


#print_file_content(path_to_file)