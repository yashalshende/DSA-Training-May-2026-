maths = (int(input("Enter marks for maths: ")))
chemistry = (int(input("Enter marks for chemistry: ")))
biology = (int(input("Enter marks for biology: ")))

total = int(maths) + int(chemistry) + int(biology)
print("Total marks: ", total)

percentage = total * 100 / 300
print("Percentage: ", percentage)

if maths >= 35 and chemistry >= 35 and biology >= 35:
    print("Overall: Pass")
else:
    print("Overall: Fail")

gender = input("Enter your gender (M/F): ")
if percentage >= 65 and gender == "M": 
    print("Eligible for placement")
else:
    print("Not eligible for placement")