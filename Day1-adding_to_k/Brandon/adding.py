# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

from copy import deepcopy

def is_k_a_sum(list_of_nums,k):
    # Using set because of the benefit that it provides in lookup with in operator
    sum_set = set()
    # Looping using the index and number to identify which number is itself
    for index,number in enumerate(list_of_nums):
        # copying to not modify the original
        copied_list = deepcopy(list_of_nums)
        # deleting the current number to keep from adding it to itself
        del copied_list[index]
        for num in copied_list:
            # adding and providing the sum
            sum_set.add(sum([num,number]))
            # if k is in the set then we return true
            if k in sum_set:
                return True
    return False


if __name__ == "__main__":
    assert True == is_k_a_sum([10, 15, 3, 7],17)
    assert False == is_k_a_sum([10, 15, 3, 6],17)
    assert False == is_k_a_sum([10, 15, 3, 8, 234, 345, 6345, 234, 67, 391], 400)