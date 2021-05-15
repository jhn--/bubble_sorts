def bubble(L):
    """Bubble sort
    
    Parameters:
    L (list): Unsorted list.
        
    Returns:
    L (list): Sorted list.
    """
    swapped = None # set to None to kick start the sort.
    while swapped == True or swapped == None: 
        # if previous iteration of bubble sort was done, or this is the first time we're attempting to sort
        swapped = False # now we set to False as no swap was done yet.
        for i in range(len(L)-1): # loop through
            if L[i] > L[i+1]: # if the current element is larger than the next element
                (L[i], L[i+1]) = (L[i+1], L[i]) # swap the elements
                swapped = True # as the elements has been swapped, set swapped to True
    return L
