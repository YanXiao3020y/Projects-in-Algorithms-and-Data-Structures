# Example file: next_fit.py
from CFloat import CFloat


# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    index = 0
    free_space.append(1.0)  # initialize the first bin

    for i in range(len(items)):
        cur_bin_space = free_space[index]
        new_item_space = items[i]
        if CFloat(cur_bin_space) < CFloat(new_item_space):
            rest_space = 1.0 - items[i]
            free_space.append(rest_space)
            index += 1
        else:
            free_space[index] -= items[i]

        assignment[i] = index
