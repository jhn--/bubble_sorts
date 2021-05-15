def mit_bubble(L):
    """Bubble sort
    
    Parameters:
    L (list): Unsorted (eventually sorted) list.
    swap (boolean): Whether list's elements have been swapped before, serves as an indicator on whether we're done sorting.
    
    Returns:
    L (list): Sorted list.
    """
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                (L[j-1], L[j]) = (L[j], L[j-1])
    return L
