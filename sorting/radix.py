def radix(sample, i):
    arr_len = len(sample)
    if i == 0:
        max = 0
        for i in range(arr_len):
            if sample[i] > max:
                max = sample[i]
        max_iterations = len(str(max))
    temp_arr = []
    for i in range(10):
        for j in range(arr_len):
            if (int(sample[j]/10**i))%10 == i:
                temp_arr.append(sample[j])
    if max_iterations > i:
        return sample(temp_arr, i + 1, max_iterations)
    return temp_arr