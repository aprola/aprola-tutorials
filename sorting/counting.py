sample = [9, 7, 6, 2, 1, 3, 3, 8]
def countingsort(sample):
    # print("sample array ", sample)
    # step 2
    max = 0
    for i in sample:
        if max < i:
            max = i
    # step 2.1 
    count_array = [0] * (max+1)
    # print("count array ", count_array)
    # step 3
    result_array = [0] * len(sample)
    # print("result array ", result_array)
    # step 4
    for i in sample:
        count_array[i] += 1
    # print("count array after counting", count_array)
    #step 5
    for i in range(1, len(count_array)):
        count_array[i] = count_array[i] + count_array[i-1]
    # print("count array after summing", count_array)
    #step 6
    for i in sample:
        index = count_array[i]
        result_array[index - 1] = i
        count_array[i] -= 1
        # print("ra: ", result_array, 
        # " ca:", count_array)
    # print("result array ", result_array)
    return result_array
    