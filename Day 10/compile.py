# import re  # re module is used for regular expression operations

# count = 0  # To count the number of matches found

# # Pattern to search
# pattern = re.compile("function")

# # Text where we want to search the pattern
# matcher = pattern.finditer(
#     "A function in python is defined by a def statement. "
#     "The general syntax looks like this: def function-name "
#     "(Parameter list): statements, i.e. the function body. "
#     "The parameter python list consists of none or more parameters."
# )

# # Loop through all matched results
# for i in matcher:
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences:", count)

# import re

# count = 0

# matcher = re.finditer("Hi", "HiHiHiHi")

# for i in matcher:  # Loop executes 4 times
#     count += 1
#     print(i.start(), "...", i.end(), "...", i.group())

# print("The number of occurrences:", count)

# import re
# obj = input("Enter a string: ")
# objmatcher = re.finditer("Hi", obj)
# for i in objmatcher:
#     print(i.start(), "...", i.end(), "...", i.group())

# import re
# a= input("Enter a stringto perform match operation: ")   
# mtch = re.match(a, "python is very important language")
# print(mtch)
# if mtch!=None:
#     print("Match found at beginning level")
#     print(mtch.start(), "...", mtch.end())
# else:   
#     print("Match not found at beginning level")

# import re
# a= input("Enter a stringto perform match operation: ")   
# mtch = re.fullmatch(a, "pythonisvery")
# print(mtch)
# if mtch!=None:
#     print("Match found")
#     print(mtch.start(), "...", mtch.end())
# else:   
#     print("Full match not found")

# import re
# s = input("Enter aMail id: ")   
# mtch = re.fullmatch(s, "\w[\w\.-]+@gmail[.]com")
# print(mtch)
# if mtch!=None:
#     print("Valid Mail id")
# else:   
#     print("Invalid Mail id")

#  import re
# mo = input("Enter Mobile Number: ")   
# mtch = re.fullmatch(mo, "\d{10}")
# print(mtch)
# if mtch!=None:
#     print("Valid Mobile Number")
# else:   
#     print("Invalid Mobile Number")

# import re
# a = input("Enter a string to perform match operation: ")
# mtch = re.search(a, "python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print(mtch.start(), "...", mtch.end()," ...", mtch.group())
# else:   
#     print("There is no matching anywhere in the string")

# import re
# mtch = re.findall('[0-9a-z]',"abch3hj3h4h5h6h7h8h9" )
# print(mtch)

# import re
# obj = re.sub(r'[a-zA-Z]', 'X', '2345 ABCD fabc deff')
# print(obj)

# import re
# obj = re.subn(r'[0-7]', '@', 'ab3gd6nkl7h8h9')
# print(obj)
# print("the String is=", obj[0])
# print("the number of replacements=", obj[1])

# Write a python program to extract all mobile numbers
# from a given string and print them in a list

# import re

# f1 = open("input.txt","r")
# f2 = open("output.txt","w")

# # Read full data from input.txt into a string variable
# data = f1.read()

# # Pattern for 10 digit mobile numbers
# mobile_numbers = re.findall(r"\b[6-9][0-9]{9}\b", data)

# # Print mobile numbers in list
# print(mobile_numbers)

# # Write mobile numbers into output.txt
# f2.write(str(mobile_numbers))

# # Close both files
# f1.close()
# f2.close()

# print("Mobile numbers extracted successfully.")

# Program to print the number of lines, words and characters
# present in the given file

# import os
# import sys

# fname = input("Enter File Name: ")

# if os.path.isfile(fname):
#     print("File exists:", fname)
# else:
#     print("File does not exist:", fname)
#     sys.exit(0)

# f = open(fname, "r")

# lcount = 0
# wcount = 0
# ccount = 0

# for line in f:
#     lcount = lcount + 1
#     ccount = ccount + len(line)

#     words = line.split()
#     wcount = wcount + len(words)

# f.close()

# print("The number of Lines:", lcount)
# print("The number of Words:", wcount)
# print("The number of Characters:", ccount)

class Graph:
    def __init__(self, vertices):
        self.V = vertices

        self.matrix = [[0 for column in range(vertices)] for row in range(vertices)]

    def display(self):
        for row in self.matrix:
            print(row)
    
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("Graph after adding edges:")
g.display()

g.remove_edge(3, 4)

print("Graph after removing edge:")
g.display()