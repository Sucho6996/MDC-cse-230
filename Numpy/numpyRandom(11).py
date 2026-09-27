import numpy as np

rand=np.random.default_rng()#seed=1

print("Integer: \n",rand
      .integers(low=1,high=101, size=(3,2)))

print("Floats: \n",rand
      .uniform(low=-1,high=1, size=(3,2)))

#by default uniform run between 0 and 1

ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])

rand.shuffle(ages)
print("Suffled ages: \n", ages)

fruits=np.array(["Apple","Banana","Coconut","Orange","Pineapple"])
print("Random fruit: \n", rand.choice(fruits))