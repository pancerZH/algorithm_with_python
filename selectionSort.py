import random


def find_smallest(num_arr):
    smallest = num_arr[0]
    smallest_index = 0
    for i in range(1, len(num_arr)):
        if num_arr[i] < smallest:
            smallest = num_arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(num_arr):
    order_arr = []
    for i in range(len(num_arr)):
        smallest_index = find_smallest(num_arr)
        order_arr.append(num_arr.pop(smallest_index))
    print(order_arr)

num_arr = []
for i in range(20):
    num_arr.append(i)
random.shuffle(num_arr)
print(num_arr)
selection_sort(num_arr)
