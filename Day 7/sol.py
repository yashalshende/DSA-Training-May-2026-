

# # Reverse each word in a string

# s = input("Enter a string: ")

# words = s.split()

# result = []

# for word in words:
#     result.append(word[::-1])

# print(" ".join(result))

# s = "Nikhil is a good boy"
# print(s[::-1])

# Check for valid parentheses

# s = input("Enter brackets: ")

# stack = []

# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }

# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     elif ch in ")}]":
#         if not stack or stack[-1] != pairs[ch]:
#             print("Invalid")
#             break
#         stack.pop()
# else:
#     if not stack:
#         print("Valid")
#     else:
#         print("Invalid")

#find the first non-repeating charecter in a string
# s = input("Enter a string: ")
# char_count = {}
# for ch in s:
#     char_count[ch] = char_cou/nt.get(ch, 0) + 1
# for ch in s:
#     if char_count[ch] == 1://
#         print("First non-repeating character: ", ch)
#         break
# else:
#     print("No non-repeating character found.")        

#insertion sort implementation
# arr = [5, 3, 4, 1, 2]

# n = len(arr)

# for i in range(1, n):
#     key = arr[i]
#     j = i - 1

#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key

# print("Sorted array:", arr)

# name = input("Enter your name:")

# print("my name is:", name)

# Find all duplicate elements in a list

# arr = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# seen = set()
# duplicates = set()

# for num in arr:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)

# print(list(duplicates))

# students = [
#     {'name': 'Amit', 'marks': 75},
#     {'name': 'Ravi', 'marks': 90},
#     {'name': 'Neha', 'marks': 60}
# ]

# students.sort(key=lambda x: x['marks'])

# print(students)

# Remove all elements from a dictionary
student = {
    "name": "Yashal",
    "age": 21,
    "marks": 85
}

student.clear()

print(student)