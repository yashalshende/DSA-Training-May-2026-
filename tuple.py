mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)
print(type(mytuple))

# mytuple[2]= "grape"
# Tuples are unchangeable, so you cannot change, add or remove items after the tuple has been created. But we can convert the tuple into a list, change the list, and convert the list back into a tuple.

init_tuple = ()

print(init_tuple.__len__())
#Output: 0

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
print(init_tuple_a == init_tuple_b) 
#Output: True

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
print(init_tuple_a + init_tuple_b)
#Output: ('1', '2', '3', '4')

l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)

init_tuple = ('Python') * 3
print(type(init_tuple))


# init_tuple = (1,) * 3
# init_tuple[0] = 2
# This will raise a TypeError because tuples are immutable and do not support item assignment.

init_tuple = ((1,2),) * 7
print(len(init_tuple[3:8]))

mydict = {
101: "nikhil",
102: "suraj",
"103": "vivek",
"104": "golu",
101: "suraj",
102: "suraj"
}
print(mydict)

mydict[102]="peter"
print(mydict)

for X in mydict:
    print(X)

for X in mydict.values():
    print(X)

for X, Y in mydict.items():
    print(X, Y)

mydict["mobile_no"] = 1234567890
print(mydict)

mydict.pop(101)
print(mydict)

a = {(1,2):1,(2,3):2,(4,5):3}
print(a[(4,5)])

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1
print(arr)
sum = 0
for k in arr:
    sum += arr[k]
print(sum)

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)
sum = 0
for k in my_dict:
    sum += my_dict[k]
print (sum)

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum = 0
for k in my_dict:
    sum += my_dict[k]
print (sum)
print(my_dict)

box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates['box']))

dict ={'c': 97, 'a': 96, 'b': 98}
for _ in sorted(dict):
    print(dict[_])

rec = {'name': 'python', 'age': 30,}
r = rec.copy()
print(id(r)==id(rec))
print(id(r))
print(id(rec))

rec = {'name': 'python', 'age': 30, "address": "delhi", "country": "india"}
id1 = id(rec)
print(id1)
del rec
rec= {'name': 'python', 'age': 30, "address": "delhi", "country": "india"}
id2 = id(rec)
print(id2)
print(id1==id2)

# find the key with the maximum value in a dictionary
my_dict = {'a': 10, 'b': 20, 'c': 15}
max_key = max(my_dict, key=my_dict.get)
print(max_key) 
 # Output: 'b'   

#reverse a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)
# Output: {1: 'a', 2: 'b', 3: 'c'}

#find the key with the minimum value in a dictionary
my_dict = {'a': 10, 'b': 20, 'c': 5}
min_key = min(my_dict, key=my_dict.get)
print(min_key)
# Output: 'c'   

#remove duplicates from a list using a dictionary
my_list = [1, 2, 3, 2, 4, 1, 5]
unique_dict = {item: None for item in my_list}
unique_list = list(unique_dict.keys())
print(unique_list)
# Output: [1, 2, 3, 4, 5] 

#count the frequency of each element in a list using a dictionary
my_list = ['a', 'b', 'c', 'a', 'b', 'a']
frequency_dict = {}
for item in my_list:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1
print(frequency_dict)
# Output: {'a': 3, 'b': 2, 'c': 1} 

num = 123
a =num % 10
num = num // 10
b = num % 10
c = num // 10
rev = a * 100 + b * 10 + c*1
print(rev)

#123456 = 654321
num = 123456
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
f = num // 10
rev = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f * 1
print(rev)

Amount = int(input("Please Enter Amount for Withdraw: "))
print("100 notes = ", Amount // 100)
print("50 notes = ", (Amount % 100) // 50)
print("20 notes = ", ((Amount % 100) % 50) // 20)
print("10 notes = ", (((Amount % 100) % 50) % 20) // 10)
print("5 notes = ", ((((Amount % 100) % 50) % 20) % 10) // 5)
print("2 notes = ", ((((Amount % 100) % 50) % 20) % 10 % 5) // 2)
print("1 notes = ", ((((Amount % 100) % 50) % 20) % 10 % 5) % 2 //1) 

#maximum consecutive ones
arr = [1, 1, 0, 1, 1, 1]
max_count = 0
count = 0
for num in arr:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)

#merge intervals
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals.sort(key=lambda x: x[0])
merged = []
for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
print(merged)

#count substrings
s = "abc"
count = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        count += 1      
print(count)    

i=1
while i<=5:
    print(i)
    i+=1

    