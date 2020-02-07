# Week 6
## Exercise 1
1. Create a python file with 3 functions:
    1. def print_file_content(file) that can print content of a csv file to the console
    2. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
        1. rewrite the function so that it gets an arbitrary number of strings instead of a list
    3. def read_csv(input_file) that take a csv file and read each row into a list
2. Add a functionality so that the file can be called from cli with 2 arguments
    1. path to csv file
    2. an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
3. Add a --help cli argument to describe how the module is used

[Se Exercise 1](https://github.com/UlrikHolm/Sem4Python/blob/master/week6/exercise1.py)


## Exercise 2
Create a module called utils.py and put the following functions inside:

1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
2. second takes a path to a folder and write all filenames recursively (files of all sub folders to)
3. third takes a list of filenames and print the first line of each
4. fourth takes a list of filenames and print each line that contains an email (just look for @)
5. fifth takes a list of md files and writes all headlines (lines starting with #) to a file Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.

[Se Exercise 2](https://github.com/UlrikHolm/Sem4Python/blob/master/week6/utils.py)

