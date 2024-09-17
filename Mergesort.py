def Sort2List(list1: list, list2: list) -> list:
    """This function merge and sort already sorted lists that contain nummbers.

    Args:
        list1 (list): Sorted first list 
        list2 (list): Sorted second list

    Returns:
        list: Merge and sorted list
    """    
    if not list1:  
        return list2
    if not list2:  
        return list1
    
    
    if list1[0] <= list2[0]:
        return [list1.pop(0)] + Sort2List(list1, list2)  
    else:
        return [list2.pop(0)] + Sort2List(list1, list2)  

                

def MergeSort(Unsortred_list: list) -> list:
    """This function sort numbers usnig the merge sort algorithm.

    Args:
        Unsortred_list (list): Unsorted list of numbers

    Returns:
        list: Sorted list
    """    
    if len(Unsortred_list) == 0 or len(Unsortred_list) == 1:
        return Unsortred_list
    
    if len(Unsortred_list) == 2:
        if Unsortred_list[0] > Unsortred_list[1]:
            return Unsortred_list[::-1]
        
        elif Unsortred_list[0] == Unsortred_list[1]:
            return Unsortred_list
        
        else:
            return Unsortred_list
        
        
    mid  = int(len(Unsortred_list)/2)
    
    return Sort2List(MergeSort(Unsortred_list[:mid]), MergeSort(Unsortred_list[mid:]))
