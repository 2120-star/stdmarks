name = input("enter student name: ")
college = input("Enter college: ")
city = input("Enter city: ")
no_ofsubjects = int(input("Enter number of subjects: "))
total = 0

for i in range(0, no_ofsubjects):
    marks = int(input("enter marks: "))
    total = total + marks

print("Total marks: ", total)

avg = total / no_ofsubjects
print("Average marks: ", avg)

if avg >= 60:
    print("pass")
else:
    print("fail")