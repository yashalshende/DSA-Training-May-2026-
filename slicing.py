# name = "prashantjha" # this is our string
# #012345678910


# print(name[0]) #p
# print(name[1]) #r
# print(name[-1]) #a
# #print(name[15])
# print(name[0:5]) # end-1, 5-1= 4 prash
# print(name[1:])  #rashantjha
# print(name[:5])  # 5-1=4 prash
# print(name[:]) #prashantjha
# print(name[1:8:2])#'''8-1=7= rsat
# print(name[::-1]) # reverse of string

# s = "Python are High level programming Language"

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# name = "yashal"
# sal = 5000000
# age = 22
# print("{} sal is {} age is{}".format(name, sal,age)) 
# print("{0} sal is {1} age is {2}".format(name, sal, age)) 
# print("{x} sal is {y} age is{z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")

# name ="yashal"
# for i in name: #i=0:y
#     print(i)

# #i/p =yashal
# #o/p = yashl
# # WAP to remove duplicates from the string 

# name ="yashal"
# newname = ""
# N = len(name) #6
# for i in range(N-1,-1,-1): 
#     newname += name[i]
# print(newname)

# #palindrome check
# name = "yashal"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("Palindrome")
# else:    print("Not Palindrome")

# #Count Vowels and Consonants
# name = "yashal"
# print(name)
# vowels = 0
# consonants = 0
# for i in name:
#     if i in "aeiouAEIOU":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels:", vowels)
# print("Consonants:", consonants)

# #Anagram check
# name1 = "yashal"
# name2 = "lahsay"
# print(sorted(name1))
# print(sorted(name2))
# if sorted(name1) == sorted(name2):
#     print("Anagram")
# else:    print("Not Anagram")

# #Pangram check
# sentence = "The quick brown fox jumps over the lazy dog"
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     if char not in sentence.lower():
#         print("Not Pangram")
#         break
# else:    print("Pangram")

# # count words in a string
# sentence = "The quick brown fox jumps over the lazy dog"
# words = sentence.split()
# print("Number of words:", len(words))

# #reverse words in a string
# sentence = "The quick brown fox jumps over the lazy dog"
# words = sentence.split()
# reversed_sentence = " ".join(reversed(words))
# print("Reversed sentence:", reversed_sentence)

# #BODMAS check
# a=50
# b=20
# c=10
# d=10
# print((a+b)*c/d)
# print(a+(b*c)/d)
# print(a+b*c/d)

# # #TCS Question


# # message = input("Enter the message: ")

# # count = 0

# # for ch in message:
# #     if not ch.isalnum():   # checks special characters and spaces
# #         count += 1

# # print("Number of special characters and whitespaces:", count)

# #Title Case
# sentence = "the quick brown fox jumps over the lazy dog"
# title_case_sentence = sentence.title()
# print("Title Case:", title_case_sentence)

# #Check for subsquence
# def is_subsequence(s1, s2):
#     it = iter(s2)
#     return all(char in it for char in s1)   
# s1 = "abc"
# s2 = "ahbgdc"
# print(is_subsequence(s1, s2))  # Output: True


# print('prashantjha777'.isalnum()) #True
# print('prashantjha'.isalpha()) #True
# print('777f'.isdigit()) #True
# print('sdsdsdsd'.islower()) #True
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))
# print("yashal".find("ha"))
# print("yashal".index("ha"))
# print("yashal".count("a"))

# #Nested loops
# for i in range(1,4):
#     for j in range(1,4):
#         print (i,end=" ")
#     print()

# # n=int(input("Enter the number of rows: "))
# # for i in range(1, n + 1):
# #     for j in range(1, n + 1):
# #         print(chr(64 + j), end=" ")
# #     print()    

# # n=int(input("Enter the number of rows: "))
# # for i in range(1, n + 1):
# #     for j in range(1, 1 + i):
# #         print("*", end=" ")
# #     print()        

# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n+2-i):
#         print(chr(64 + j), end=" ")
#     print()            

# import time
# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     print(" "*(n-i), end=" ")
#     for j in range(1, i+1):
#         time.sleep(0.5)
#         print("*", end=" ")
#     print()

#product of array except self
arr = [1, 2, 3, 4]
result = [1] * len(arr)
for i in range(1, len(arr)):
    result[i] = result[i - 1] * arr[i - 1]
R = 1
for i in range(len(arr) - 1, -1, -1):
    result[i] *= R
    R *= arr[i]
print(result)

#move zeros to end
arr = [0, 1, 0, 3, 12]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1
for i in range(j, len(arr)):
    arr[i] = 0
print(arr)

tuple.py