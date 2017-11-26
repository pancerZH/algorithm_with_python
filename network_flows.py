'''导入队列'''
from collections import deque
start = 's'
end = 't'


'''找到一条通路'''
def find_next(graph_res, stack):
    for i in graph_res[stack[-1]]:
        if i in stack:
            continue
        stack.append(i)
        if i == end:
            return True
        if find_next(graph_res, stack) == False:
            stack.pop()
        else:
            return True
    return False


'''找到这组流的最小值'''
def cal_min_flow(graph_res, stack):
    weight_of_flow = graph_res[stack[0]][stack[1]]
    for i in range(1, len(stack)-1):
        weight_of_flow = min(weight_of_flow, graph_res[stack[i]][stack[i+1]])
    return weight_of_flow


'''在流图中修改权值，在残余图中修改权值并添加反向回路'''
def update_graph(graph_flow, graph_res, stack):
    weight = cal_min_flow(graph_res, stack)
    for i in range(len(stack)-1):
        # 更新残余图
        graph_res[stack[i]][stack[i+1]] -= weight
        if graph_res[stack[i]][stack[i+1]] == 0:
            graph_res[stack[i]].pop(stack[i+1])
        if stack[i] in graph_res[stack[i+1]]:
            graph_res[stack[i+1]][stack[i]] += weight
        else:
            graph_res[stack[i+1]][stack[i]] = weight
        # 更新流图
        if stack[i+1] in graph_flow[stack[i]]:
            graph_flow[stack[i]][stack[i+1]] += weight
        else:
            graph_flow[stack[i+1]][stack[i]] -= weight


'''实现未知名字的算法'''
def find_min_flow(graph, graph_flow, graph_res):
    stack = deque([start])
    while find_next(graph_res, stack):
        update_graph(graph_flow, graph_res, stack)
        stack.clear()
        stack.append(start)


def get_max_flow(graph_flow):
    sum = 0
    for i in graph_flow[start]:
        sum += graph_flow[start][i]
    return sum

'''
建立图、流图、残余图，依靠字典实现
当我完成绝大部分代码才发现，graph根本没有派上用场
或许graph可以做为一个吉祥物，或者一个对照，或者用来取代graph_res
'''
def main():
    graph = {}
    graph['s'] = {}  # s是起点
    graph['s']['a'] = 3
    graph['s']['b'] = 2
    graph['a'] = {}
    graph['a']['b'] = 1
    graph['a']['d'] = 4
    graph['a']['c'] = 3
    graph['b'] = {}
    graph['b']['d'] = 2
    graph['c'] = {}
    graph['c']['t'] = 2
    graph['d'] = {}
    graph['d']['t'] = 3
    graph['t'] = {}
    # t是终点
    graph_flow = {}
    graph_flow['s'] = {}  # s是起点
    graph_flow['s']['a'] = 0
    graph_flow['s']['b'] = 0
    graph_flow['a'] = {}
    graph_flow['a']['b'] = 0
    graph_flow['a']['d'] = 0
    graph_flow['a']['c'] = 0
    graph_flow['b'] = {}
    graph_flow['b']['d'] = 0
    graph_flow['c'] = {}
    graph_flow['c']['t'] = 0
    graph_flow['d'] = {}
    graph_flow['d']['t'] = 0
    graph_flow['t'] = {}
    # t是终点
    graph_res = {}
    graph_res['s'] = {}  # s是起点
    graph_res['s']['a'] = 3
    graph_res['s']['b'] = 2
    graph_res['a'] = {}
    graph_res['a']['b'] = 1
    graph_res['a']['d'] = 4
    graph_res['a']['c'] = 3
    graph_res['b'] = {}
    graph_res['b']['d'] = 2
    graph_res['c'] = {}
    graph_res['c']['t'] = 2
    graph_res['d'] = {}
    graph_res['d']['t'] = 3
    graph_res['t'] = {}
    # t是终点

    find_min_flow(graph, graph_flow, graph_res)
    print(graph_flow)
    print(graph_res)
    print('max flow : {}'.format(get_max_flow(graph_flow)))

if __name__ == '__main__':
    main()