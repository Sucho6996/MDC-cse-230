stu=[]
dict={}
max=0
maxMarks=0
n=int(input("How many record you wanna add?: "))

for i in range (n):
    roll=input("\nEnter Roll: ")
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))
    tuple=(roll,name,marks)
    stu.append(tuple)

print("\n\n\nDetails of the students: ")
for i in range (n):
    dict[stu[i][2]]=dict.get(stu[i][2],0)+1
    print("\nRoll: ",stu[i][0],"\nName: ",stu[i][1],"\nMarks: ",stu[i][2])

for marks in dict.keys():
    if(dict.get(marks)>max):
        max=dict.get(marks)
        maxMarks=marks

print("\n\n\nMode of this dataset is: ",maxMarks)
