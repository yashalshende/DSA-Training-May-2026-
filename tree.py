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
def first_missing_positive(nums):
    smallest = 1

    while smallest in nums:
        smallest += 1

    return smallest


arr = [3, 4, -1, 1]
print(first_missing_positive(arr))

# find the smallest missing positive integer in a list of unsorted integers

def smallest_missing_positive(arr):
    num = 1

    while num in arr:
        num += 1

    return num


arr = [7,8,9,11,12]
print(smallest_missing_positive(arr))