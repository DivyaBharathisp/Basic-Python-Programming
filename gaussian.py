# import the required libraries  
import random  
import matplotlib.pyplot as plt  
    
# store the random numbers in a   
# list  
nums = []  
mu = 100
sigma = 5
    
for i in range(100):  
    temp = random.gauss(mu, sigma) 
    nums.append(temp)  
        
# plotting a graph  
plt.plot(nums)  
plt.savefig('Gaussian.png')
