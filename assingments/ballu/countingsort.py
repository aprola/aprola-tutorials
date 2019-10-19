def counting_sort(arr1, max_value):
    m = max_value + 1
    count = [0] * m

    for a in arr1:
        count[a] += 1
    
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            arr1[i] = a
            i += 1
    return arr1   

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))