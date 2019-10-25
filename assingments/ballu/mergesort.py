def  mergesort(marr):
    marr_length = len(marr)
    if marr_length > 1:
        mid = marr_length//2
        return marr
        left = mergesort(marr[:mid])
        right = mergesort(marr[mid:])
    
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                marr[k] = left[i]
                i+=1
            else:
                marr[k] = right[j]
                j+=1
            k+=1
        
            while i < len(left):
                marr[k] = left[i]
                i+=1
                k+=1
            while j < right[j]:
                marr[k] = right[j]
                j+=1
                k+=1
        
            