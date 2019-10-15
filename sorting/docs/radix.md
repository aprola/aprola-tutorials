# 1 take sample array
sample = [101, 789, 39, 449, 008, 850, 457]
# 2 sort based on units place, using any sorting algo.
sample = [850, 101, 457, 008, 789, 39, 449]
# 3 sort based on tens place, using any sorting algo.
sample = [101, 008, 39, 449, 850, 457, 789]
# 4 sort based on hunderds place, using any sorting algo.
sample = [008, 039, 101, 449, 457, 789, 850]

# 5 sort based on thousands place, using any sorting algo.
sample = [008, 039, 101, 449, 457, 789, 850]

# sort algo
sample = [101, 789, 39, 449, 008, 850, 457]
    to get units place x%10
    array = {
        0: [850],
        1: [101],
        2: [],
        3: [],
        .
        .
        .
        9: [789, 39, 449]
    }
    850, 101, .... 789, 39, 449