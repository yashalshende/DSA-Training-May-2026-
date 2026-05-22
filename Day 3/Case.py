chr = ord(input("Enter a character: "))
if chr >= 65 and chr <= 90:
    print("Uppercase")
elif chr >= 97 and chr <= 122:
    print("Lowercase")
elif chr >= 48 and chr <= 57:
    print("Digit")
else:
    print("Special character")