from utils.random import randomArrayGenerator2
from sorting.mergesort import mergesort
from assingments.nishu.mergesort import mergeSort

nos = int(input("enter sample size: "))
sample = randomArrayGenerator2(nos)
# sample = [3,1,2,5,0,4]
print("sample is : ", sample)
# result = mergesorlt(sampe)
result = mergeSort(sample)
print("sorted sample is : ", result)