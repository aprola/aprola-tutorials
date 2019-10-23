from utils.random import randomArrayGenerator2
from utils.random import randomArrayGeneratorWithDuplicates
from sorting.mergesort import mergesort
from sorting.quicksort import quicksort
from sorting.radix import radix
from sorting.counting import countingsort
from assingments.nishu.mergesort import mergeSort
from assingments.ballu.countingsort import counting_sort
from assingments.linsifa.quicksort import quickSort  as lin_quicksort



nos = int(input("enter sample size: "))
# max = int(input("enter max value: "))
sample = randomArrayGenerator2(nos)
# sample = [3,1,2,5,0,4]
print("sample is : ", sample)
# result = counting_sort(sample,nos-1)
lin_quicksort(sample)
print("sorted sample is : ", sample)