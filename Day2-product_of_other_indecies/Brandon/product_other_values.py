from copy import deepcopy
from functools import reduce

def product_of_other_vals(list_of_numbers):
    vals = []
    for i in range(len(list_of_numbers)):
        this_copy = deepcopy(list_of_numbers)
        del this_copy[i]
        vals.append(reduce(lambda cur,nex: cur*nex,this_copy,1))
    return vals


if __name__ == "__main__":
    assert product_of_other_vals([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_of_other_vals([3, 2, 1]) == [2, 3, 6]