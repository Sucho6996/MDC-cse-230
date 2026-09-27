n=int(input("How many Marks you wanna entered: "))

marks=[] #[75,85.95]

for i in range(n):
    mark=int(input("Enter the marks: "))
    marks.append(mark)

marks.sort()

m=len(marks) #len=6

mid = m // 2 #mid=3 but we are accessing 4th element here

if m % 2 == 0:
    median=(marks[mid - 1] + marks[mid]) / 2
else:
    median=marks[mid]

print("Median: ", median)


