def bubble(L, swap=None):
    """Bubble sort function

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
        i = 0
        swap = False
        while i < len(L):
            ii = i + 1
            if L[i] > L[ii]:
                (L[i], L[ii]) = (L[ii], L[i])
                swap = True
            i += 1
            if i == len(L)-1:
                return bubble(L, swap)
    else:
        return L
