import time

def quicksort(arr, start=0, end=0):
    # a, b
    pivot = (end or len(arr)) - 1
    j = pivot - 1
    i = start
    # print("first step a: ", i, j, pivot,arr[0:pivot + 1])
    while(i<j):
        # c
        while(arr[i] < arr[pivot] and i < pivot):
            i+=1
        # print("stoped i at: ", i)
        while(arr[j] >arr[pivot] and j > 0):
            j-=1
        # print("stoped j at: ", j)
        if  i < j and arr[i] > arr[j]:
            # print("swapped i and j : ", arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > arr[pivot]:
        # print("swapped i and pivot : ", arr[i], arr[pivot])
        arr[i], arr[pivot] = arr[pivot], arr[i]
    if (i>1):
        quicksort(arr,0,i)
    
    if (pivot-i > 1):
        quicksort(arr, i+1, pivot+1)

def quicksort_with_recursion(arr):
    # a, b
    stack_box = [ [0,0] ]
    time_now = time.time()
    while(True):
        if len(stack_box) > 0:
            v = stack_box.pop()
        else:
            break
        pivot = (v[1] or len(arr)) - 1
        j = pivot - 1
        i = v[0]
        # print("first step a: ", i, j, pivot,arr[0:pivot + 1])
        while(i<j):
            # c
            while(arr[i] <= arr[pivot] and i < pivot):
                i+=1
            # print("stoped i at: ", i)
            while(arr[j] >= arr[pivot] and j > 0):
                j-=1
            # print("stoped j at: ", j)
            if  i < j and arr[i] > arr[j]:
                # print("swapped i and j : ", arr[i], arr[j])
                arr[i], arr[j] = arr[j], arr[i]
            # import time
            # time.sleep(1)
            # print(i,"," ,j, " - ", arr[i],",", arr[j], "p", arr[pivot])
        if arr[i] > arr[pivot]:
            # print("swapped i and pivot : ", arr[i], arr[pivot])
            arr[i], arr[pivot] = arr[pivot], arr[i]
        # print("*", end="")
        if (i>1):
            stack_box.append([0,i])
        
        if (pivot-i > 1):
            stack_box.append([i+1,pivot+1])
        # import time
        # time.sleep(1)
        x = time.time()
        if (x - time_now > 1):
            time_now = time.time()
            print( len(stack_box))