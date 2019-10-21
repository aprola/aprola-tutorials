import time
from sorting.heapsort import heapsort

# 1 take sample.
# sample =[10, 9, 209, 15, 27, 35, 826]

def bucketsort(sample):
    # 2. take buckets of size K (10 for radix)
    # [] list, () tuple, {} dictionary
    buckets = {}
    for i in range(10):
        buckets[i] = []
        
    sample_length = len(sample)
    print("sample length: ", sample_length)

    max = 0
    for i in range(sample_length):
        if max < sample[i]:
            max = sample[i]
    
    digits_in_max_value = len(str(max))

    
    ## 3.1 if numbers are intergers.
    for i in range(sample_length):
        index = sample[i]//(10**(digits_in_max_value-1))
        # print('index is ', index, sample[i], i, digits_in_max_value)
        buckets[index].append(sample[i])
    # print("buckets: ", buckets)
    # time.sleep(2)

    # 4. sort the values in bucket in buckets. 
    for i in range(10):
        if len(buckets[i]) > 1:
            # print("heapify", buckets[i])
            heapsort(buckets[i])
            # print("sorted", buckets[i])
    
    sorted_bucket = []
    # print("sorted start", sorted_bucket)
    for i in range(10):
        # print("merrging ", buckets[i])
        sorted_bucket += buckets[i]
        # print("after merge ", sorted_bucket)
    
    return sorted_bucket




# def bucketsort_recursive(sample, place=0):
#     # 2. take buckets of size K (10 for radix)
#     # [] list, () tuple, {} dictionary
#     buckets = {}
#     for i in range(10):
#         buckets[i] = []
        
#     sample_length = len(sample)
#     print("sample length: ", sample_length)

#     max = 0
#     for i in range(sample_length):
#         if max < sample[i]:
#             max = sample[i]
    
#     digits_in_max_value = len(str(max))

    
#     ## 3.1 if numbers are intergers.
#     for i in range(sample_length):
#         index = sample[i]%(10**(digits_in_max_value-1))
#         # print('index is ', index, sample[i], i, digits_in_max_value)
#         buckets[index].append(sample[i])
#     # print("buckets: ", buckets)
#     # time.sleep(2)

#     # 4. sort the values in bucket in buckets. 
#     for i in range(10):
#         if len(buckets[i]) > 1:
#             # print("heapify", buckets[i])
#             heapsort(buckets[i])
#             # print("sorted", buckets[i])
    
#     sorted_bucket = []
#     # print("sorted start", sorted_bucket)
#     for i in range(10):
#         # print("merrging ", buckets[i])
#         sorted_bucket += buckets[i]
#         # print("after merge ", sorted_bucket)
    
#     return sorted_bucket