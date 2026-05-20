# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []

#     def __str__(self, level=0):
#         ret = "\t" * level + repr(self.data) + "\n"
#         for child in self.child:
#             ret += child.__str__(level + 1)
#         return ret

#     def addChild(self, object):  
#         self.child.append(object) 
#         print("Tree node added successfully")

# rootNode = Tree("Drinks")
# hot = Tree("Hot")
# cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee = Tree("Coffee")
# NonAlcoholic = Tree("Non-Alcoholic")
# Alcoholic = Tree("Alcoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(Tea)
# hot.addChild(Coffee)
# cold.addChild(NonAlcoholic)
# cold.addChild(Alcoholic)

# print(rootNode)

# # Tree Node Example in Python

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# # Creating Nodes
# N1 = Node("N1")
# N2 = Node("N2")
# N3 = Node("N3")
# N4 = Node("N4")
# N5 = Node("N5")
# N6 = Node("N6")
# N7 = Node("N7")
# N8 = Node("N8")

# # Connecting Nodes
# N1.left = N2
# N1.right = N3

# N2.left = N4
# N2.right = N5

# N3.right = N6

# N4.left = N7
# N4.right = N8


# # Function to print tree (Preorder Traversal)
# def preorder(node):
#     if node:
#         print(node.value, end=" ")
#         preorder(node.left)
#         preorder(node.right)

# print("Preorder Traversal of Tree:")
# preorder(N1)

#Array Rotation
# def rotate_array(arr, k):
#     n = len(arr)
#     k = k % n  # Handle cases where k is greater than n

#     # Rotate the array using slicing
#     return arr[-k:] + arr[:-k]
# print(rotate_array([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

#remove leading zeros from a list of integers
# def remove_leading_zeros(arr):
#     index = 0

#     while index < len(arr) and arr[index] == 0:
#         index += 1

#     return arr[index:]

# print(remove_leading_zeros([0, 0, 1, 2, 0, 3, 0]))  # Output: [1, 2, 3]

# Find the first missing positive integer:
# def first_missing_positive(nums):
#     smallest = 1

#     while smallest in nums:
#         smallest += 1

#     return smallest


# arr = [3, 4, -1, 1]
# print(first_missing_positive(arr))

# # find the smallest missing positive integer in a list of unsorted integers

# def smallest_missing_positive(arr):
#     num = 1

#     while num in arr:
#         num += 1

#     return num


# arr = [7,8,9,11,12]
# print(smallest_missing_positive(arr))

# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# # Insert node in BST
# def insertNode(rootNode, nodeValue):
#     if rootNode.data is None:
#         rootNode.data = nodeValue

#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild, nodeValue)

#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild, nodeValue)

#     return "The node has been inserted successfully"


# # Search node in BST
# def searchNode(rootNode, nodeValue):
#     if rootNode is None:
#         print("The value is not found")
#         return

#     if rootNode.data == nodeValue:
#         print("The value is found")

#     elif nodeValue < rootNode.data:
#         if rootNode.leftChild is None:
#             print("The value is not found")
#         else:
#             searchNode(rootNode.leftChild, nodeValue)

#     else:
#         if rootNode.rightChild is None:
#             print("The value is not found")
#         else:
#             searchNode(rootNode.rightChild, nodeValue)


# # Preorder Traversal: Root -> Left -> Right
# def preOrderTraversal(rootNode):
#     if rootNode is None:
#         return

#     print(rootNode.data, end=" ")
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)


# # Inorder Traversal: Left -> Root -> Right
# def inOrderTraversal(rootNode):
#     if rootNode is None:
#         return

#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data, end=" ")
#     inOrderTraversal(rootNode.rightChild)


# # Postorder Traversal: Left -> Right -> Root
# def postOrderTraversal(rootNode):
#     if rootNode is None:
#         return

#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data, end=" ")


# # Create root node
# rootNode = BSTNode(70)

# # Insert nodes according to your tree image
# insertNode(rootNode, 50)
# insertNode(rootNode, 90)
# insertNode(rootNode, 30)
# insertNode(rootNode, 60)
# insertNode(rootNode, 80)
# insertNode(rootNode, 100)
# insertNode(rootNode, 20)
# insertNode(rootNode, 40)
# insertNode(rootNode, 10)


# print("Inorder Traversal:")
# inOrderTraversal(rootNode)

# print("\nPreorder Traversal:")
# preOrderTraversal(rootNode)

# print("\nPostorder Traversal:")
# postOrderTraversal(rootNode)


# print("\n\nSearch Result:")
# searchNode(rootNode, 40)

# a =int(input("enter First Number:"))
# b =int(input("enter Second Number:"))
# try:
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
#     except ValueError:
#     print("Error: Invalid input. Please enter numeric values.")

# import logging

# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)

# try:
#     a = int(input("enter first integer no"))
#     b = int(input("enter second integer no"))
#     print(a / b)

# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)

# print("Logging Level is set up. Check 'newfile.txt' for log details.")

# import csv

# # Open employee.csv file in append mode
# f = open("employee.csv", "a", newline="")

# # Create csv writer object
# a = csv.writer(f)

# # Uncomment this line only one time to add headings
# # a.writerow(["EmpID", "Emp Name", "Emp Age"])

# # Taking employee details from user
# empid = int(input("Enter your EmpID: "))
# empName = input("Enter employee name: ")
# age = int(input("Enter employee age: "))

# # Writing data into CSV file
# a.writerow([empid, empName, age])

# # Closing the file
# f.close()

# print("File has been created and data inserted successfully.")

import csv

# Open CSV file in append mode
f = open("student.csv", "a", newline="")

# Create CSV writer object
writer = csv.writer(f)

# Column names
writer.writerow([
    "studId",
    "studName",
    "phy",
    "Chem",
    "math",
    "Total",
    "Percentage",
    "Result"
])

# Taking input from user
studId = int(input("Enter Student ID: "))
studName = input("Enter Student Name: ")

phy = int(input("Enter Physics Marks: "))
chem = int(input("Enter Chemistry Marks: "))
math = int(input("Enter Math Marks: "))

# Calculate total
total = phy + chem + math

# Calculate percentage
percentage = total / 3

# Check pass or fail condition
if phy >= 40 and chem >= 40 and math >= 40:
    result = "Pass"
else:
    result = "Fail"

# Write student data into CSV file
writer.writerow([
    studId,
    studName,
    phy,
    chem,
    math,
    total,
    percentage,
    result
])

# Close the file
f.close()

print("Student record has been created successfully.")