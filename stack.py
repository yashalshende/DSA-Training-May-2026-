# import math

# # Input
# n = int(input())
# areas = list(map(int, input().split()))

# count = 0

# # Check perfect square areas
# for area in areas:
#     root = int(math.sqrt(area))
    
#     if root * root == area:
#         count += 1

# # Output
# print(count)

# L

#write a program to access each charecter  of a string in forward and backward direction by using while loop?    
# Access each character of a string in forward and backward direction using while loop

# s = input("Enter a string: ")

# print("Forward direction:")
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# print("Backward direction:")
# i = len(s) - 1
# while i >= 0:
#     print(s[i])
#     i -= 1

# Find the missing character from sent string

# stringSent, stringRec = input().split()

# for ch in stringSent:
#     if stringSent.count(ch) != stringRec.count(ch):
#         print(ch)
#         break

# v = ['a','e','i','o','u']
# w = input("enter the word where we will seach for vowel: ")     
# # w= prashantjha

# found = []
# for i in w:
#     if i in v:
#         found.append(i)
# print("Vowels found:", found)
# print('unique vowels found:', len(set(found)), 'from the given word:', w)

# Find distances within the given range

# num, start, end = map(int, input().split())
# distances = list(map(int, input().split()))

# for d in distances:
#     if start <= d <= end:
#         print(d, end=" ")

# import datetime
# #datetime formatting
# date = datetime.datetime.now()
# print("it's no : {:%d/%m/%Y %H:%M:%S}".format(date))

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x == z)
# print(x!=z)

# s = [1,4,9,16,25,36,49,64,81,100]
# val=[2**i for i in range(1,6)]
# print(val)

# #Dictionay Comprehension
# squares = {x:x*x for x in range(1,6)}
# print(squares)

# a,b=[int(x) for x in input("enter two numbers: ").split()]
# print("product is :", a*b)


# a,b,c= [float(x) for x in input("Enter three numbers: ").split(',')]
# print("The sum of the three numbers is: ", a+b+c)

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item > 400:
#         print("Expensive item: ", item)
#         continue
#     print("Affordable item: ", item)

# while True:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == 'admin' and password == 'admin':
#         print("Login successful")
#         break
#     else:
#         print("Login failed. Please try again.")


# def tower_of_hanoi(n, source, helper, destination):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return

#     tower_of_hanoi(n - 1, source, destination, helper)
#     print(f"Move disk {n} from {source} to {destination}")
#     tower_of_hanoi(n - 1, helper, source, destination)


# # Main code
# n = int(input("Enter number of disks: "))

# tower_of_hanoi(n, "A", "B", "C")

import time

class Tower:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
        self.temp = 0

    def tower(self, n):
        self.A.append(n)

    def show(self, step):
        time.sleep(1)
        print("A=", self.A, "     ", "B=", self.B, "     ", "C=", self.C)
        print(step, "Completed================\n")

    def pass1(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        self.show("Pass One")

    def pass2(self):
        self.temp = self.A.pop(0)
        self.B.append(self.temp)
        self.show("Pass Two")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.insert(0, self.temp)
        self.show("Pass Three")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        self.show("Pass Four")

    def pass5(self):
        self.temp = self.B.pop(0)
        self.A.append(self.temp)
        self.show("Pass Five")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.insert(0, self.temp)
        self.show("Pass Six")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.insert(0, self.temp)
        self.show("Pass Seven")


obj = Tower()

obj.tower(3)
obj.tower(2)
obj.tower(1)

print("Initial Towers")
print("A=", obj.A, "     ", "B=", obj.B, "     ", "C=", obj.C)
print()

obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
