# 1 take sample.
sample =[10, 9, 209, 15, 27, 35, 826]

# 2. take buckets of size K (10 for radix)
buckets = { 0:[], 1: [], 2:[], ...... 9: [] }

# 3. get the max number and count the digits in it.

# 4. place numbers in buckets based on the following ways:
## 4.1 if numbers are intergers.
        . place into buckets based on the digit position(like units, tens, hunderds...)
## 4.2 if numbers are floating
        . place into buckets based on the the position from left. ie(decimal place 1, decimal place 2, ....)
<!-- controvestial -->
# 5. sort the values in bucket in buckets. 
## do it using sorting technique
## do it recursively.


<!-- workout -->
sample =[10, 9, 209, 15, 27, 35, 826]
bucket:
0 -> 10
1
2
3
4
5 -> 15, 35
6 -> 826
7 -> 27
8
9




