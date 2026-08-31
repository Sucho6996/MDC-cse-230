stu=[]

n=int(input("How many record you wanna add?: "))

for i in range (n):
    roll=input("\nEnter Roll: ")
    name=input("Enter Name: ")
    marks=input("Enter Marks: ")
    tuple=(roll,name,marks)
    stu.append(tuple)

print("\n\n\nDetails of the students: ")
for i in range (n):
    print("\nRoll: ",stu[i][0],"\nName: ",stu[i][1],"\nMarks: ",stu[i][2])