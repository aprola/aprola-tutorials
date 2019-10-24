def  mergesort(arr):
    arr_length = len(arr)
    if (arr_length != 1):
        return arr
    left = mergesort(arr[:arr_length//2])
    right = mergesort(arr[arr_length//2:])
    
    i=j=0
    result = []
    
    for _ in range(0, arr_length):
        
        if (i > len(left) - 1):
            result = result + right[j:]
            return result
        
        if (i > len(right) - 1):
            result = result + left[i:]
            return result

        if (left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    return result

        
   
