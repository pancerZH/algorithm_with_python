def binary_search(num_list, num):  # 假定列表元素升序排列
    low = 0
    high = len(num_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if num_list[mid] == num:
            return mid
        elif num_list[mid] <= num:
            low = mid + 1
        else:
            high = mid - 1

    return None

list1 = [1, 3, 5, 7, 9]
print(binary_search(list1, 1))
print(binary_search(list1, -1))
