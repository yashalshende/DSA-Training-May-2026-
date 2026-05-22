#function

def hello():
    print("Hello, World!")
hello()
hello()

def arithmetic():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div
print (arithmetic())

#how mayntypes of argument we pass in a function?
#1. Positional arguments
#2. Keyword arguments
#3. Default arguments
#4. Variable-length arguments

#keyword arguments
def crdentials(username, password):
  if username == password:
    print("login successful")
  else:
    print("login failed")
crdentials(username = "admin", password = "admin")