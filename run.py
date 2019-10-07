from utils.random import randomArrayGenerator2
from sorting.mergesort import mergesort


nos = int(input("enter sample size: "))
sample = randomArrayGenerator2(nos)
# sample = [3,1,2,5,0,4]
print("sample is : ", sample)
result = mergesort(sample)
print("sorted sample is : ", result)