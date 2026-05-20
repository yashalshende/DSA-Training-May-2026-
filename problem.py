# input = "abababab"
# substring = "ab"
# left = 0
# right = 1
# while(right< len(input))
#     string = input(left:right+1)
# if(string == substring):
#     count += 1
#     right+=1
#     left+=1
#     print(count)



# i = 1
# while i<=5:
#     print(i)
#     i+=1

# def arithmatic():
#     a= int(input("Enter value of a:"))
#     b= int(input("Enter value of b:"))
#     sum = a+b
#     sub= a-b
#     div= a/b
#     mul = a*b
#     return sum, sub, div, mul

# print(arithmatic()) #Tupke(values does not change) possible to written the multiple values
# print("Arithmatic =", result)
# How many types of arguments we pass in a function

# 1. positional argument
# 2. default argument
# 3. keyeword argument
# 4. variable length argument / variable number of argument

# 1.positional argument

# def arithmatic(a,b):
#     a= int(input("Enter value of a:"))
#     b= int(input("Enter value of b:"))
#     sum = a+b
#     sub= a-b
#     div= a/b
#     mul = a*b
#     return sum, sub, div, mul

# print(arithmatic(5,5)) #Tupke(values does not change) possible to written the multiple values
# print("Arithmatic =", result)

# 2. keyword argument

# def arithmatic():
#     a= int(input("Enter value of a:"))
#     b= int(input("Enter value of b:"))
#     sum = a+b
#     sub= a-b
#     div= a/b
#     mul = a*b
#     return sum, sub, div, mul

# print(arithmatic()) #Tupke(values does not change) possible to written the multiple values
# print("Arithmatic =", result)

# 3: default argument

# def cityName(city = "Nagpur")
#     print(cityName)

# print("ngp")
# print("mumbai")
# print()

# 3. keyword argument

# def credentials(username, password)
#     if(username == "admin" and password == "123")
#     print("login successfullly")
#     else("invalid credentials")
# credentials(username="admin", password="admin")

# def cityaName(*name):
#     print(name)


# cityaName("Nagpur", "pune", "Mumbai", "Chennal")

#modularity in function
# import sys

# def add():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a+b)

# def sub():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a-b)

# def div():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a/b)

# def mul():
#     a = int(input("Enter value of A:"))
#     b = int(input("Enter value of B:"))
#     print(a*b)

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Division")
#     print("4. Multiplication")
#     print("5. Exit")
#     choice = int(input("Enter your choice :"))
#     if choice ==1:
#         add() #calling function
#     elif choice ==2:
#         sub()
#     elif choice ==3:
#         div()
#     elif choice ==4:
#         mul()
#     elif choice == 5:
#         sys.exit()

# def findBiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0]
#     for index in range(1,len(sampleArray)):
#         if sampleArray[index] > biggestNumber:
#             biggestNumber = sampleArray[index]
#     print(biggestNumber)

#     sampleArray = [5,7,9,2,3,4]
#     findBiggestNumber(sampleArray)

#     def foo (array):
#         sum =0 
#         product= 1
#         for i in every array:

#             sum +=1
#             for i in array:
#                 product += 1
#                 print("sum = "+ str(sum+)", (product = )"+ str(product) )

# def simpleArray(ar)
#     sum = 0
#     for i in range (len(ar)):
#         sum = sum + ar[i]
#     return sum
# if __name__ == '__main__':


# city = input("Enter your city")
# scity=city.strip()
# if scity=='Hyderabad':
#     print("Hello Hyderabadi.. Abab")
# elif scity == "Chennai":
#     print("Hello madrasi.. Vanakkam")
# elif scity == "Bangalore":
#     print("Hello Bangladeshi.. Subhodaya")
# else:
#     print("Your entered city is invalid")

# def compareTriplates(a,b):
#     alice = 0
#     bob = 0
#     for i, j in zip (range(len(a)), range(len(b))):
#         if a[i] > b[j]:
#             alice += 1
#         if a[i] < b[j]:
#             bob += 1
#         if a[i] == b[j]:
#             pass
#     return alice, bob


# input = "aaabbbbccceeeeee"
# target = "a3b4c335"
# dlc={}
# for ele in input:
#     if ele not in dlc:
#         dlc[ele]=0
#         dlc[ele]+=1
#     print(dlc)
#     ans=""
#     for ele in dlc:
#         ans+= ele+str(dlc[ele])
#     print(ans)

basicSalary = 20000

HRA = basicSalary * 0.2
TA = basicSalary * 0.3
DA = basicSalary * 0.45

print(basicSalary + HRA + TA + DA)

