dict={}

n=int(input("How many record you wanna add?: "))

for i in range (n):
    roll=input("\nEnter Roll: ")
    name=input("Enter Name: ")
    dict[name]=roll

name=input("\nEnter name to get roll: ")

print("Roll of ",name," is ",dict.get(name))