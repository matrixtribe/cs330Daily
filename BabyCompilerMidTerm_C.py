# import re for regular expressions
import re
# import pathlib for file path IO
from pathlib import Path

# assign folder path to input doc
data_folder = Path("/Users/ToA/Desktop/CS330/Assignments/Midterm_project_spring_2019/Midterm_project/")

# assign file name
file_to_open = data_folder / "CLevel.java"

# read file into program
c_level_file = open(file_to_open, 'r')

# read file in to contents variable
contents = c_level_file.read()
print(contents)

# remove all block comments
pattern = re.compile(r"/\*.*?\*/", re.S)
contents = re.sub(pattern, "", contents)
print("block comments removed")
print(contents)

# remove all in-line comments
pattern = re.compile(r"//.*")
contents = re.sub(pattern, "", contents)
print("in-line comments removed")
print(contents)

# remove all import statements
pattern = re.compile(r"import.*;")
contents = re.sub(pattern, "", contents)
print("import statements removed")
print(contents)

# remove all print statements
pattern = re.compile(r"System\.out\.println\(.*\);")
contents = re.sub(pattern, "", contents)
print("print statements removed")
print(contents)

# remove assignment statements
pattern = re.compile(r"(String|boolean|int)(\s|\w)*=(\s|\w)*(;|\"\w+\");?")
contents = re.sub(pattern, "", contents)
print("removed assignment statements")
print(contents)

# remove all white-spaces
pattern = re.compile(r"\s*")
contents = re.sub(pattern, "", contents)
print("all white-space removed")
print(contents)

# remove arithmetic expressions
pattern = re.compile(r"\w*=\w*[+|\-|%|/]\w*;")
contents = re.sub(pattern, "", contents)
print("removed arithmetic expressions")
print(contents)

# remove main
pattern = re.compile(r"(public|private|protected)(static|final)(void|\w{2,25})(\w{2, 25})?main\(String\[\]args\){}")
contents = re.sub(pattern, "", contents)
print("removed main")
print(contents)

# remove class
pattern = re.compile(r"(class)(\w{2,25}){}")
contents = re.sub(pattern, "", contents)
print("removed class")
print(contents)
if contents == '':
    print("C code correctly compiled!")


