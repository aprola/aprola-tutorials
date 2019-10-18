def counting_sort(array, maxval):
    x = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             
    i = 0
    for a in range(m):            
        for i in range(count[a]): 
            array[i] = a
            i += 1
    return array
