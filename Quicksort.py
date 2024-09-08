def QuickSort1(Unsorted_list: list) -> list:
    """This function use quicksort method to sort list that contain numbers in ascending order

    Args:
        Unsorted_list (list): A list containing numbers

    Returns:
        list: Sorted list
    """
    if len(Unsorted_list) == 1 or len(Unsorted_list) == 0:
        return Unsorted_list
    
    pivot = Unsorted_list[-1]
    Smaller_list = []
    Larger_List = []
    
    for item in Unsorted_list[:-1]:
        if item >= pivot:
            Larger_List.append(item)
            
        else:
            Smaller_list.append(item)
            
    small = QuickSort1(Smaller_list)
    large = QuickSort1(Larger_List)
    
    return small + [pivot] + large




def QuickSort2(Unsorted_list: list) -> list:
    """This function use quicksort method to sort list that contain numbers in ascending order

    Args:
        Unsorted_list (list): A list containing numbers

    Returns:
        list: Sorted list
    """
    if len(Unsorted_list) == 1 or len(Unsorted_list) == 0:
        return Unsorted_list
    
    pivot = Unsorted_list[0]
    i = 1
    j = len(Unsorted_list) - 1
    
    try:
        for _ in range(len(Unsorted_list[1:])):
            if j > i:
                try:
                    for num1 in range(len(Unsorted_list[1:])):
                        if Unsorted_list[i+num1] > pivot:
                            i += num1
                            raise StopIteration
                
                except StopIteration:
                    pass
                
                try:
                    for num2 in range(len(Unsorted_list[1:])):
                        if Unsorted_list[j-num2] < pivot:
                            j -= num2
                            raise StopIteration
                
                except StopIteration:
                    pass
                
                if j < i:
                    temp = Unsorted_list[j]
                    Unsorted_list[j] = pivot
                    Unsorted_list[0] = temp
                    raise StopIteration
                    
                
                temp = Unsorted_list[i]
                Unsorted_list[i] = Unsorted_list[j]
                Unsorted_list[j] = temp
                
    except StopIteration:
        pass
    
    smaller_list = QuickSort2(Unsorted_list[:j])
    larger_list = QuickSort2(Unsorted_list[j+1:])
    
    return smaller_list + [pivot] + larger_list
        

 
