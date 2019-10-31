def bucketsort(sample):

    buckets = {}
    for i in range(10):
        buckets[i] = []
        
    array_length = len(sample)
    print("sample length: ", array_length)

    max = 0
    for i in range(array_length):
        if max < sample[i]:
            max = sample[i]
    
    digits_in_max_value = len(sample(max))

    for i in range(array_length):
        index = sample[i]//(10**(digits_in_max_value-1))
        buckets[index].append(sample[i]

    for i in range(10):

        if len(buckets[i]) > 1:
    
            insertion(buckets[i])
            
    
    sorted_bucket = []
    for i in range(10):

        sorted_bucket += buckets[i]
    
    return sorted_bucket
