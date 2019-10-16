from utils.random import randomArrayGenerator2
from utils.random import randomArrayGeneratorWithDuplicates
from sorting.mergesort import mergesort
from sorting.quicksort import quicksort
from sorting.radix import radix
from sorting.counting import countingsort
from assingments.nishu.mergesort import mergeSort



nos = int(input("enter sample size: "))
max = int(input("enter max value: "))
sample = randomArrayGeneratorWithDuplicates(nos, 0, max)
# sample = [3,1,2,5,0,4]
print("sample is : ", sample)
result = quicksort(sample)
print("sorted sample is : ", result)