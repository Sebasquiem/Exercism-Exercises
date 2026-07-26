def find(search_list, value):
    search_list.sort()
    min = 0
    max = len(search_list) -1
    while min <= max:
        mid = (min + max) // 2
        if  search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            min = mid + 1
        elif search_list[mid] > value:
            max = mid - 1
    raise ValueError("value not in array")
   
        
