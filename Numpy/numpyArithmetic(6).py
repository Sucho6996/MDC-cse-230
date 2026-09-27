import numpy as np

#scalar arithmatic
print("\n\nscalar arithmatic")
arr=np.array([1,2,3])
print("Array: ",arr)
print("Addition ",arr + 1)
print("Substarctions ",arr - 2)
print("Multiplication ",arr * 3)
print("Division ",arr / 4)
print("Exponent ",arr ** 5)

#vectorized math function
print("\n\nvectorized arithmatic")
arr=np.array([1.01,2.21,3.19])
print("Array: ",arr)
print("Sqrt: ",np.sqrt(arr))
print("Round: " ,np.round(arr)) 
#np.floor(arr)-> round down
#np.ceil(arr)-> round up
print("PI: ",np.pi)

#Exercise: take a array of radiuses and 
# compute their area using numpy

#Element Wise Arithmetic
print("\n\nElement Wise arithmatic")
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print("Array 1: ",arr1)
print("Array 2: ",arr2)
print("Addition: ",arr1 + arr2)
print("Substarctions: ",arr1 - arr2)
print("Multiplication: ",arr1 * arr2)
print("Division: ",arr1 / arr2)
print("Exponent: ",arr1 ** arr2)

#Comparison Operater
print("\n\nComparison Operater")
scores=np.array([91,55,100,73,82,64])
print("Is Full marks? ")
print(scores==100) #try if anyone got full marks
print("Is Cutoff Cleared? ")
print(scores>=60) #try if who pass
#No credit for who didn't cleared
scores[scores<60]=0
print(scores)