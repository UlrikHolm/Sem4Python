import csv
import os
import argparse
import sys

path1 = '.'
out1 = 'files.csv'
out2 = 'filesAndFolders.csv'
#Exercise 2.1

def files_in_folder (path,output_file):
    files = os.listdir(path)
    with open(output_file, 'w') as file_object:
        for file in files:
            file_object.write("%s\n" % file)

#files_in_folder(path1,out1)

#Exercise 2.2

def recursive_folder (path,output_file):
    with open(output_file, 'w') as file_object:
        for dirName, subdirList, fileList in os.walk(path):
            file_object.write('\nDir: %s' % dirName)
            for fname in fileList:
                file_object.write('\n\t%s' % fname)
    
#recursive_folder(path1,out2)

#Exercise 2.3
lst_files = ['file1.csv', 'file2.csv', 'file3.csv']

def print_files_first_line(list_of_files):
    for file in list_of_files:
        with open(file, 'r') as f:
           lines =  f.readline()
           print(lines[0].rstrip())

#print_files_first_line(lst_files)

#Exercise 2.4

def print_files_email(list_of_files):
    for file in list_of_files:
        with open(file, 'r') as f:
            lines =  f.readlines()
            for line in lines:
                if '@' in line:
                    print('Email: ' + line.rstrip() + ' In file: ' + file)

# print_files_email(lst_files)

#Exercise 2.5

lst_md_files = ['mdfile1.md']

def print_files_headline(list_of_files,output_file):
    for file in list_of_files:
        with open(file, 'r') as f:
            lines =  f.readlines()
            with open(output_file, 'a') as file_object:
                for line in lines:
                    if '#' in line:
                            file_object.write(line)

md_out = 'mdfile1Copy.md'
#print_files_headline(lst_md_files,md_out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that check files for headers(#) and write the line to a file')
    parser.add_argument('pathlist', help='Paths to the file to read from')
    parser.add_argument('file', help='File to write to')
    args = parser.parse_args()
#    print(parser.parse_args())
#    print(args.pathlist.split(','))
    print_files_headline(args.pathlist.split(','),args.file)