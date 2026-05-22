# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data   # instance variable
#         self.next = None

# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def addNode(self, value):
#         self.node = Node(value)

#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node  
#             self.tail = self.node       # shifting pointer

#     def addNodeBeginning(self, value):
#         print("Add node beginning")

#         self.node = Node(value)

#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.node.next = self.head
#             self.head = self.node

#     def addNodeBetween(self, value, position):
#         print("Add Node in between")

#         self.node = Node(value)

#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#             return

#         temp = self.head
#         count = 1

#         while temp is not None and count < position - 1:
#             temp = temp.next
#             count += 1

#         if temp is None:
#             print("Position not found")
#         else:
#             self.node.next = temp.next
#             temp.next = self.node

#             if self.node.next is None:
#                 self.tail = self.node

#     def addNodeEnd(self, value):
#         print("Add Node at End")
#         self.addNode(value)

#     def displayNode(self):
#         temp = self.head

#         if temp is None:
#             print("Linked List is empty")
#             return

#         while temp is not None:
#             print(temp.data, '|', '->', end=' ')
#             temp = temp.next

#         print("None")


# if __name__ == '__main__':
#     object = LinkedList()

#     while True:
#         print('\n1. Add Node LinkedList : ')
#         print('2. Add Node in Beginning : ')
#         print('3. Add Node in Between : ')
#         print('4. Add Node in End : ')
#         print('5. Display Linked List : ')
#         print('6. Exit : ')

#         ch = int(input('Enter your choice: '))

#         if ch == 1:
#             value = int(input('Enter value for node: '))
#             object.addNode(value)
#             print('Node added successfully in single LinkedList')

#         elif ch == 2:
#             value = int(input('Enter value for Node: '))
#             object.addNodeBeginning(value)
#             print('Node added successfully at beginning')

#         elif ch == 3:
#             value = int(input('Enter value for Node: '))
#             position = int(input('Enter position after which node should be inserted: '))
#             object.addNodeBetween(value, position)
#             print('Node added successfully in between')

#         elif ch == 4:
#             value = int(input('Enter value for Node: '))
#             object.addNodeEnd(value)
#             print('Node added successfully at end')

#         elif ch == 5:
#             object.displayNode()
    
#         elif ch == 6:
#             sys.exit()

#         else:
#             print("Invalid choice")

#factorial Solution using recursion

# def factorial(num):
#     if num <=1:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(5))

# #capitalizeFirst Solution using recursion

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result

#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))
        
# from tensorflow import string


# def power(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         return base * power(base, exp - 1)
    
# print(power(2, 0))
# print(power(2, 2))
# print(power(2, 4))

# #prodctofArray Solution using recursion

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     else:
#         return arr[0] * productOfArray(arr[1:])
    
# print(productOfArray([1, 2, 3]))
# print(productOfArray([1, 2, 3, 10]))

#reverse solution using recursion

# def reverse(strng):
#     if len(strng) <=1:
#         return strng
#     return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])

# print(reverse('python'))
# print(reverse('appmillers'))

#recursiveRange Solution using recursion

# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     else:
#         return num + recursiveRange(num - 1)

# print(recursiveRange(6))    

# def isPalindrome(strng):
#     if len(strng) <= 1:
#         return True
#     if strng[0] != strng[-1]:
#         return False
#     return isPalindrome(strng[1:-1])
# print(isPalindrome('racecar'))

# someRecursive solution

# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return False
    
#     if cb(arr[0]) == False:
#         return someRecursive(arr[1:], cb)
    
#     return True


# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True


# print(someRecursive([1, 2, 3, 4], isOdd))  # True
# print(someRecursive([4, 6, 8, 9], isOdd))  # True
# print(someRecursive([4, 6, 8], isOdd))     # False


numCards = int(input())
cards = list(map(int, input().split()))

max_product = cards[0] * cards[1]
winning_sum = cards[0] + cards[1]

for i in range(numCards):
    for j in range(i + 1, numCards):
        product = cards[i] * cards[j]

        if product > max_product:
            max_product = product
            winning_sum = cards[i] + cards[j]

print(winning_sum)

