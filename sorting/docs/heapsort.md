### 1. take sample array
sample = [9, 7, 6, 2, 1, 3, 8]
### 2. make it look like a tree. ??

# root = 0  <- index
# root->left = root_index*2 + 1
# root->right = root_index*2 + 2
# parent of index => int((child_index -1)/2)

   ref -> 0  1  2  3  4  5  6
sample = [9, 7, 6, 2, 1, 3, 8]

                          9(0)
              7(1)                   6(2)
        2(3)       1(4)       3(5)          8(6)

    x(7)     8  9       10   11     12  13      14  

### 3. when you insert a new item into the tree 
###    make sure you have high value in the parent

3.1 take index i = 0. think if i advances you placed a new item in tree.

3.2 if a item is inserted make sure its less than parent or swap with parents till root

### 4. after the hax heap is constructed. we need to swap root with the last item. and repeat
