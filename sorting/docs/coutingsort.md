### 1. take sample array
sample = [9, 7, 6, 2, 1, 3, 3, 8]
### 2. take max value and create count array of size (max + 1)
sample = [9, 7, 6, 2, 1, 3, 3, 8]
max = 9
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
### 3. make an result array of size n
result = [0, 0, 0, 0, 0, 0, 0, 0]
### 4. increase count array based on the occurence of item in input
count = [0, 1, 1, 2, 0, 0, 1, 1, 1, 1]
### 5. for each item in count array increase value to the sum of previous
    ref [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = [0, 1, 2, 4, 4, 4, 5, 6, 7, 8]
### 6. starting from (end/begin) of array iterate and update the result
###    and decrease the count array values.
    --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = [0, 1, 2, 4, 4, 4, 5, 6, 7, 8]

sample = [9, 7, 6, 2, 1, 3, 3, 8]
 index-> [0, 1, 2, 3, 4, 5, 6, 7]
### 7. sorted array from above values
 index-> [0, 1, 2, 3, 4, 5, 6, 7]
result = [0, 0, 0, 0, 0, 0, 0, 8]