def bucketSort(sample): 
    bucket = [] 
    for i in range(len(sample)): 
        bucket.append([])
        
    for j in sample: 
        index_b = int(10 * j) 
        bucket[index_b].append(j) 
    
    for i in range(len(sample)): 
        bucket[i] = sorted(bucket[i])
        
    k = 0  
    for i in range(len(sample)): 
        for j in range(len(bucket[i])): 
            sample[k] = bucket[i][j] 
            k += 1
    return sample