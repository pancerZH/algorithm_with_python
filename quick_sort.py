def quick(arr):  # 升序排列
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick(less) + [pivot] + quick(greater)

arr1 = [10, 3, 7, 9, 2]
print(quick(arr1))