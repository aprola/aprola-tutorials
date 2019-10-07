def  mergesort(arr):
    arr_length = len(arr)
    if (arr_length < 1):
        return arr
    # print('left', arr[:arr_length//2], 'right', arr[arr_length//2:])
    left = mergesort(arr[:arr_length//2])
    right = mergesort(arr[arr_length//2:])
    # todo: mergeme
    i = 0
    j = 0
    result = []
    # half = arr_length//2 # floor of a division
    for _ in range(0, arr_length):
        # print('result', result)
        # print('i:', i, '-j:', j, 'left', left, 'right', right, 'arraylen', arr_length)
        # print('bef ame here', half)
        
        if (i > len(left) - 1):
            result = result + right[j:]
            # print('returned result', result)
            return result
        elif (j > len(right) - 1):
            result = result + left[i:]
            # print('returned result', result)
            return result

        if (left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    return result



    


# alist = [12, 57, 16, 51, 23, 00, 96, 36]
# print('before sorting', alist)
# result = mergesort(alist)
# print('after sorting', result)