from utils.random import randomArrayGenerator2
from utils.random import randomArrayGeneratorWithDuplicates
from sorting.mergesort import mergesort
from sorting.quicksort import quicksort
from sorting.radix import radix
from sorting.counting import countingsort
from assingments.nishu.mergesort import mergeSort
from assingments.ballu.countingsort import counting_sort
from assingments.ballu.mergesort import mergesort


nos = int(input("enter sample size: "))
# max = int(input("enter max value: "))
sample = randomArrayGenerator2(nos)
# sample = [3,1,2,5,0,4]
print("sample is : ", sample)
result = mergesort(sample)
print("sorted sample is : ", result)