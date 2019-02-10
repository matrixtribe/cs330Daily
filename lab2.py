# Due: February 11th at the beginning of class

# Each of the sentences below are followed by a set of related instructions.
# After each instruction, add your code that does what's being asked, as well as
# a print statement that shows your work. Don't forget to print new lines as well,
# or your output will be a mess!

import re
import datetime

solution_separator = "\n\n****************************************\n\n"

# For example:
s0 = "This is a test"
print(s0 + "\n")

print(solution_separator)

# 1) Write a regular expression and if statement that checks if T is the first letter
pattern = r"T"
# print(re.search(pattern, s0))
if re.search(pattern, s0):
    print("It starts with 'T'!" + "\n")
else:
    print("My regex is incorrect, it should detect the 'T'!" + "\n")

print(solution_separator)

# 2) Use a regular expression to decompose the string into words and place those words into a list.
#    Extract the first word into a variable and print it
pattern = r"\s"
words = re.split(pattern, s0)
# print(words)
print("\n")
first_word = words[0]
print("The first word is: '" + first_word + "'\n")

print(solution_separator)

# 3) Split the sentence into an array of individual words called words and use a for loop to print it.
#    for each var in vars:
#        (your code here)
#
pattern = r'\s'
words = re.split(pattern, s0)
for word in words:
    print(word + "\n")

print(solution_separator)


# 4)
s1 = "Mary was born on September 17, 1986"

# a) Write a regular expression and if statement that checks if the name "Mary" in the sentence.
pattern = r"(?i)mary"
# print(re.search(pattern, s1))
m1 = re.search(pattern, s1)
if m1:
    print("The name " + m1.group() + " is in the sentence!" + "\n")
else:
    print("My regex is incorrect, it should detect 'mary'!" + "\n")

print(solution_separator)

# b) Write a regular expression and if statement that checks if the sentence contains a 4 digit number.
pattern = r"\d{4}"
# print(re.search(pattern, s1))
if re.search(pattern, s1):
    print("A 4 digit number is in the sentence!" + "\n")
else:
    print("My regex is incorrect, it should detect a four digit number!" + "\n")

print(solution_separator)

# c) Write a regular expression to extract that number into a variable b_year and print it in this sentence:
#    "The person was born in b_year."
pattern = r"\d{4}"
match = re.search(pattern, s1)
b_year = match[0]
# print(b_year)
print("\n")
print("The person was born in: '" + b_year + "'\n")

print(solution_separator)

# 5)
s2 = "The dog, named Dog, was doggedly trying to dodge the fog."

# a) Write a regular expression to match the word "dog", but not the name "Dog"
pattern = r"dog"
# b) Save the output from this match into a list and print the list to verify it is not matching anything else.
words = re.findall(pattern, s2)
print(words)
print(solution_separator)

# c) Write a regular expression to match "dog" and "Dog" using a flag (see the cheat sheet).
pattern = r"(?i)dog"
words = re.findall(pattern, s2)
print(words)
print(solution_separator)
# d) Write a regular expression to match "dog" or "fog"
pattern = r"dog|fog"
words = re.findall(pattern, s2)
# e) Print all outputs.
print(words)
print(solution_separator)

# 6)
s3 = "18785 is the 5 digit number I want not 43744, 34553, or 11111"

# a) Write a regular expression to extract the first number (try to do it without using the exact string).
pattern = r"\d{5}"
m3 = re.search(pattern, s3)
print(m3.group())
print(solution_separator)
# b) Write a regular expression to extract all numbers, store them in an array, then print the array.
pattern = r"\d{5}"
m3 = re.findall(pattern, s3)
print(m3)
print(solution_separator)

# 7) Write a regular expression to trim the left and right whitespace and print the trimmed output.
s4 = "    There is preceding white space in this sentence, and whitespace at the end        "
pattern = r"^\s+|\s+$"
m4 = re.sub(pattern, "", s4)
print(m4)
print(solution_separator)

# 8)
s5 = "junk data penguin begin tennis for 2 end begin Zelda and Link end begin Oculus Rift end no cheating by using " \
     "positional text flags"

# a) Write a regular expression to print everything from the first "begin" to the last "end".
pattern = r"begin.*end"
print(re.search(pattern, s5).group())
print(solution_separator)
# b) Write a regular expression to print only the text from the first "begin" to the first "end"
pattern = r"begin.*?end"
print(re.search(pattern, s5).group())
print(solution_separator)
# c) Write a regular expression to extract all of the text between "begin"s and "end"s into an array.
# d) Print all outputs.
pattern = re.compile(r"begin.*?end")
print(pattern.findall(s5))
print(solution_separator)

# 9)
s6 = "The date 5/17/1982 is trickier to get"
# a) Write a regular expression to extract the date.
# b) Capture the date in a variable f_date
pattern = re.compile(r"\d{1,2}/\d{1,2}/\d{4}")
f_date = pattern.search(s6).group()
# print(f_date)
# c) Split the date and store it as month, day, year
print("---- I wasn't exactly sure what you meant by '# c) Split the date and store it as month, day, year'"
      " so I did it 3 different ways\n")
print("--1--")
month = f_date.split("/").pop(0)
day = f_date.split("/").pop(1)
year = f_date.split("/").pop(2)
print(month, ",", day, ",", year)
print("\n--2--")
f_date2 = re.sub("/", ", ", f_date)
print(f_date2)
print("\n--3--")
f_date = f_date.split("/")
print(f_date)
# d) Convert the date to date format year-month-day where month and day always have 2 digits. Save the
#    result in comp_date
print("\n--Final formatted answer--")
comp_date = datetime.datetime(int(f_date[2]), int(f_date[0]), int(f_date[1]))
# e) Print comp_date
print(comp_date.strftime("%Y-%m-%d"))
print(solution_separator)

# 10) Extra Credit:
s8 = "These are some dates: 1/23/2011, 2/1/2006, 12/31/2007, 9/15/1993, 04/23/1797."

# a) Use a regex to collect the dates into a list
pattern = re.compile(r"\d{1,2}/\d{1,2}/\d{4}")
date_list = pattern.findall(s8)
# print(date_list)
# b) Use the code above to convert them into yyyy-mm-dd format.
reformatted_date_list = []
for date in date_list:
    date = date.split("/")
#    print(date)
    comp_date2 = datetime.datetime(int(date[2]), int(date[0]), int(date[1]))
#    print(comp_date2)
    reformatted_date_list.append(comp_date2)
# c) Print the dates in chronological order
reformatted_date_list.sort()
for d in reformatted_date_list:
    print(d.strftime("%Y-%m-%d"))
print(solution_separator)
