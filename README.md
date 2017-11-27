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

## Dijkstra.py
### find_lowest_cost_node(costs, processed)  
找出当前情况下开销最小的节点  
### find_lowest_weight_way(graph, costs, parent, processed)  
找到开销最小的路径  
### print_best_way(parent, node, start)  
打印开销最小路径

## broadcast.py  
### find_best_solution(states_needed, stations)
查找广播站的最小范围

## network_flows.py
### find_next(graph_res, stack)
递归函数，通过不断迭代找出一条由起点到终点的路径，存放在stack中
### cal_min_flow(graph_res, stack)
计算储存在stack中的flow的最小值(在所有边中找)
### update_graph(graph_flow, graph_res, stack)
每次找到一组flow时，都要更新graph_flow和graph_res的连接情况  
其中，graph_flow的连接情况不允许改变，如果遇到反向连接应减去相应的值；  
graph_res允许出现反向连接，也即它的连接状态是可以改变的。当边的权值为0时，应删除这条边
### find_min_flow(graph, graph_flow, graph_res)
驱动函数，用于找到一组flow和更新图
### get_max_flow(graph_flow)
依据`一个点的流入量等于其流出量`的原理，计算起点的流出量作为总的流量