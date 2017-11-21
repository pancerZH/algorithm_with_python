# algorithm_with_python
学习使用python学习算法

## binary_search.py
### binary_search(num_list, num)
使用二分查找的查找函数，num_list要求为升序排列的列表，num为要查找的数字

## selectionSort.py
### find_smallest(num_arr)
查找列表中最小数字的函数，返回最小值的索引  
### selection_sort(num_arr)
执行选择排序的函数，升序排列

## hanoi.py
### move(origin, middle, destination, left_num)
移动盘子的函数，参数依此为起始杆，过渡杆，目标杆和剩余盘子数目

## sum.py
### sum_arr(arr, start, end)
对列表中元素求和，参数依此为列表，起始位置，结束位置
### arr_num(arr, begin)
统计列表中元素的数目，参数依此为列表和起始位置
### find_max(arr, start, end)
查找列表中的最大值，参数依此为列表，起始位置，结束位置

## quick_sort.py
### quick(arr)
将列表中的元素升序排列

## BFS.py  
### person_is_seller(name)  
判断名为name的人是否为芒果销售商（名字以m结尾）  
### search(name, graph)  
从graph中自名为name的人开始搜索芒果销售商

## Dijkstra
### find_lowest_cost_node(costs, processed)  
找出当前情况下开销最小的节点  
### find_lowest_weight_way(graph, costs, parent, processed)  
找到开销最小的路径  
### print_best_way(parent, node, start)  
打印开销最小路径