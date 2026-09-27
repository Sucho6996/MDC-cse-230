stu=[]
sum=0
n=int(input("How many record you wanna add?: "))

for i in range (n):
    roll=input("\nEnter Roll: ")
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))
    tuple=(roll,name,marks)
    stu.append(tuple)

print("\n\n\nDetails of the students: ")
for i in range (n):
    sum+=stu[i][2]
    print("\nRoll: ",stu[i][0],"\nName: ",stu[i][1],"\nMarks: ",stu[i][2])

print("\n\nAverage is ",sum/n)