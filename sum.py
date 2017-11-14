def sum_arr(arr, start, end):
    if start == end:
        return arr[start]
    mid = int((start + end) / 2)
    return sum_arr(arr, start, mid) + sum_arr(arr, mid+1, end)


def arr_num(arr, begin):
    if not arr[begin:]:
        return 0
    return 1 + arr_num(arr, begin+1)


def find_max(arr, start, end):
    if start == end:
        return arr[start]
    mid = int((start + end) / 2)
    max1 = find_max(arr, start, mid)
    max2 = find_max(arr, mid+1, end)
    if max1 > max2:
        return max1
    else:
        return max2

num_arr = [1, 2, 3, 4, 5, 7, 6]
print(sum_arr(num_arr, 0, arr_num(num_arr, 0)-1))
print(find_max(num_arr, 0, arr_num(num_arr, 0)-1))
