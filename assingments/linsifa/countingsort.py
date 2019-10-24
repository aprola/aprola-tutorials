import numpy
def cs(alist):
    size = len(alist)
    result = [0] * size
    # m=max(alist)
    #print("m is", m)
    max=alist[0]
    for i in range(size):
        if alist[i] > max:
            max = alist[i]

    countlist= [0] * (max+1)
    for i in range(0, size):
        countlist[alist[i]] += 1
    
    for i in range(1, max+1):
        countlist[i] += countlist[i-1]
    
    for i in range(0, size):
        result[countlist[alist[i]]-1] = alist[i]
        countlist[alist[i]] -= 1
        i += 1
        #print("res: ", result) 
    
    for i in range(0, size):
        alist[i]=result[i]
    #     print('out: ', alist)


alist = []
alist= numpy.random.randint(1,1000,100)
#alist = [1, 27, 86, 43, 9, 8, 12, 25, 20, 6]
print("unsorted list is ", alist)
cs(alist)
print("sorted list is ", alist)