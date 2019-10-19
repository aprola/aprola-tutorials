
sample = [9, 7, 6, 2, 1, 3, 8]
# swap
# temp = s[i] 
# s[j] = s[i]
# s[i] = temp
# 01
# making a copy
# sample2<&031> = [8, 7, 6, 2, 1, 3, 9]
# sample<&031> = sample2



# swapTillRoot()

def heapsort(sample):
    parent_node = lambda i : int((i-1)/2)
    left_node   = lambda i : i*2 +1
    right_node  = lambda i : i*2 +2

    # inserting into tree virtually
    sample_length = len(sample)

    for i in range(sample_length):
        
        if i == 0:
            continue
        elif sample[i] > sample[parent_node(i)]:
            # a,b = b,a will swap a and b values
            j = i
            while (j != 0 and sample[j] > sample[parent_node(j)]):
                # print("child>parent: ", j, parent_node(j)," values: ", sample[j], sample[parent_node(j)])
                sample[j], sample[parent_node(j)] = sample[parent_node(j)], sample[j]
                j = parent_node(j)

    while sample_length > 1:
        # swap root with last item.
        sample[0], sample[sample_length-1] = sample[sample_length - 1], sample[0]

        # we have a max heap
        print('max heap: ', sample)
        
        # decrease the scope of length by 1
        sample_length -= 1
        print(sample)
        # swap from root to make to a prefect heap.
        j = 0
        while(True):
            if (sample_length > left_node(j) and sample[j] < sample[left_node(j)]):
                sample[j], sample[left_node(j)] = sample[left_node(j)], sample[j]
                print("swap left", sample[j], sample[left_node(j)])
                j = left_node(j)
            elif (sample_length > right_node(j) and sample[j] < sample[right_node(j)]):
                sample[j], sample[right_node(j)] = sample[right_node(j)], sample[j]
                print("swap right", sample[j], sample[right_node(j)])
                j = right_node(j)
            else:
                print('cond1: ',sample_length, left_node(j), sample_length>left_node(j))
                print('cond2: ',sample_length, right_node(j), sample_length>right_node(j))
                break


        # heaptify from root.
        

    # print("sorted sample", sample)



# Python program for implementation of heap Sort 
  
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapsort_geeks_for_geeks(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 