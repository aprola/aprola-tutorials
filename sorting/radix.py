def radix(sample, place=0, max_iterations=99999):
    # arr = sort_by_units()
    # print("sample: ",sample,"place: ", place, "max: ", max_iterations)
    arr_len = len(sample)
    # find the max length of array item
    if place == 0:
        max = 0
        for i in range(arr_len):
            if sample[i] > max:
                max = sample[i]
        max_iterations = len(str(max))
    temp_arr = []
    for i in range(10):
        for j in range(arr_len):
            if (int(sample[j]/10**place))%10 == i:
                temp_arr.append(sample[j])
    if max_iterations > place:
        return radix(temp_arr, place + 1, max_iterations)
    return temp_arr


# space -> O(K*n) -> O(n)
# time -> O(k*n*d) -> O(n*d)

    # arr = sort_by_tens()
    # arr = sort_by_hundreds()
    # return sorted