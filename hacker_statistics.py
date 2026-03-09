import numpy as np
np.random.seed(123)
#print(np.random.rand())
#print(np.random.randint(1,7))

#starting step
step = 50

#roll the dice
dice = np.random.randint(1,7)

if dice <= 2 :
    step = step -1
elif dice <= 5 :
    step = step + 1
else: 
    step = step + np.random.randint(1,7)

#print out dice and step
print(dice)
print(step)