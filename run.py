from utils.random import randomArrayGeneratorWithoutDuplicates
from utils.random import randomArrayGeneratorWithDuplicates
from sorting.mergesort import mergesort
from sorting.quicksort import quicksort
from sorting.radix import radix
from sorting.counting import countingsort
from sorting.bucketsort import bucketsort
from sorting.heapsort import heapsort, heapsort_geeks_for_geeks
from assingments.nishu.mergesort import mergeSort
from assingments.ballu.countingsort import counting_sort


# 
# nos = int(input("enter sample size: "))
# max = int(input("enter max value: "))
# sample = randomArrayGeneratorWithDuplicates(nos, 0, max)
# sample = randomArrayGeneratorWithoutDuplicates(nos)
# sample = [4, 8, 0, 3, 2, 1, 6, 7, 5, 9]
sample =[10, 9, 209, 15, 27, 35, 826]
print("sample is : ", sample)
# heapsort_geeks_for_geeks(sample)
result = bucketsort(sample)
print("sorted sample is : ", result)