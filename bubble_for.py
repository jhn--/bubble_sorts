def bubble(L, swap=None):
    """Bubble sort

    Parameters:
    L (list): Unsorted (eventually sorted) list.
    swap (boolean): Whether list's elements have been swapped before, serves as an indicator on whether we're done sorting.

    Returns:
    L (list): Sorted list.
    """
    print(f'{L} : {swap}')
    if len(L) == 0:
        return L
    if swap == True or swap == None:
        swap = False
        for i in range(len(L)):
            if i == len(L)-1:
                return bubble(L, swap)
            ii = i + 1
            if L[i] > L[ii]:
                (L[i], L[ii]) = (L[ii], L[i])
                swap = True
    else:
        return L
