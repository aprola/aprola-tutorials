# Mergesort

1. collect sample array: 
    [12, 57, 16, 51, 23, 00, 96, 36]
2. split array to half and reapply mergesort
3. [12, 57, 16, 51] ,[23, 00, 96, 36]
4. [12, 57] -- [16, 51] ,[23, 00], -- [96, 36]
5. [12] [57] -- [16] [51] ,[23], [00], -- [96], [36]
6. Join from bootom till top by using sorting two sorted arrays.
   1. take two pointers. 
   2. move such that smaller number to temporary array and advance.
   3. return temp array to top stack
   4. [12] [57] -- [16] [51] ,[23], [00], -- [96]
   5. [12, 57]--[16, 51],[00, 23],--[36, 96]
   6. [12, 16, 51, 57] ,[00, 23, 36, 96]
   7. [00, 12, 16, 23, 36, 51, 57, 96]


edge cases:
    [1,2, 3,4] [ 5,6,7,8]

    [3,1,2,5,0,4]
    
    [3,1,2][5,0,4]

    [3],[1,2] [5], [0, 4]
    
    [3], [1] [2],  [5], [0], [4]

    [3], [1,2],  [5], [0,4]


    [1,2, 3],  [0,4, 5]
    [0,1,2,3,4,5]