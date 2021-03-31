# # permutations
import itertools
import collections

def get_duplicate_idx(n): # n=[3, 2, 1, 3, 3, 2]

    counter=collections.Counter(n) # {'3': 3, '2': 2, '1': 1}
    # get each duplicate value list of list idx
    return [[i for i,j in enumerate(n) if j==each_value] for each_value in set(n)] # [[2], [1, 5], [0, 3, 4]] 


duplicate_idx_list = get_duplicate_idx([3, 2, 1, 3, 3, 2])
# find the permutations for the given idx
res = [len([x for x in itertools.permutations(idx, 2) if x[0]<x[1]]) for idx in duplicate_idx_list]

# find the maximum combination of permutations with 2 matrix
print (max(res))
