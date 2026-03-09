import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
# #print(np.random.rand())
# #print(np.random.randint(1,7))

# #starting step
# step = 50

# #roll the dice
# dice = np.random.randint(1,7)

# if dice <= 2 :
#     step = step -1
# elif dice <= 5 :
#     step = step + 1
# else: 
#     step = step + np.random.randint(1,7)

# #print out dice and step
# print(dice)
# print(step)

#random walk
# random_walk = [0]
# for x in range(100) :
#     step = random_walk[-1]
#     dice = np.random.randint(1,7)

#     if dice <= 2 :
#         step = step -1
#     elif dice <= 5 :
#         step = step + 1
#     else: 
#         step = step + np.random.randint(1,7)

#     if step < 0 :
#         step = 0

#     random_walk.append(step)
# print(random_walk)


# # Plot random_walk
# plt.plot(random_walk)

# # Show the plot
# plt.show()


# Initialize all_walks
all_walks = []

# Simulate random walk 500 times
for i in range(500):

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
     

    # Append random_walk to all_walks
    all_walks.append(random_walk)
 

# Print all_walks
print(all_walks[1])
print(len(all_walks))
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]    
# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()  

#Calculate the odds of reaching 60 or higher
odds = len(ends[ends >= 60]) / len(ends)
print("Odds of reaching 60 or higher:", odds)   