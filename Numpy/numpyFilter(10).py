import numpy as np

#Filtering is the process of selecting elements
#from an array based of a given condition

ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])

teens=ages[ages<20]
print("All: \n",ages)
print("Teens: \n",teens)

#adults=ages[(ages>=20) & (ages<60)] #&->and
adults=np.where((ages>=20) & (ages<60), ages, np.nan)
print("Adults: \n",adults)

sc=ages[ages>=60]
print("Senior Citizen: \n",sc)