#import numpy

def merge_sort(alist, f, l):
    if l - f >= 2:
        mid = (f + l)//2
        merge_sort(alist, f, mid)
        merge_sort(alist, mid, l)
        merge_list(alist, f, mid, l)

def merge_list(alist, f, mid, l):
        left = alist[f:mid]
        right = alist[mid:l]
        k = f
        i = 0
        j = 0
        while (f + i < mid and mid + j < l):
            if (left[i] <= right[j]):
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        if f + i < mid:
            while k < l:
                alist[k] = left[i]
                i = i + 1
                k = k + 1
        else:
            while k < l:
                alist[k] = right[j]
                j = j + 1
                k = k + 1



alist = [14, 23, 5, 1, 12, 9]

# alist = []
# n = int(input('Enter the list of numbers: '))
# for i in range (n):
#     values = int(input('enter number %d of %d: ' %(i+1, n)))
#     alist.append(values)  

#alist = []
#alist= numpy.random.randint(1,100,9)
#n = int(input('Enter the list of numbers: '))
#for i in range (n):
#values = randint(n)
    #alist.append(values)

 
merge_sort(alist, 0, len(alist))
print('Sorted list: ', alist)

