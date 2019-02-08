# WITHOUT USING STATISTICS LIBRARY

def mean_num_friends(x):
    sum=0;
    for each in x:
        sum = sum+each
    mean=sum/n
    return mean
    
def median_num_friends(x):
    x.sort()
    if n%2==0:
        median = (x[int(n/2)]+x[int(n/2)+1])/2
    else:
        median =x[int(n/2)]
    return median
    
num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
n = len(num_friends)
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))

# END WITHOUT USING STATISTICS LIBRARY

print("Above is without using inbuilt library")
print("Below is by using inbuilt library")

# WITH STATISTICS LIBRARY

import statistics

def mean_num_friends(x):
    mean = statistics.mean(x)
    return mean
def median_num_friends(x):
    median = statistics.median(x)
    return median

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))

# END WITH STATISTICS LIBRARY