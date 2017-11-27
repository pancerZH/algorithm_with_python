'''找到与当前树相邻的未处理节点中开销最小的'''
def find_lowest_cost_node(cost, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in cost:
        if cost[node] < lowest_cost and node not in processed:
            lowest_cost = cost[node]
            lowest_cost_node = node
    return lowest_cost_node


'''建立最小生成树'''
def build_min_spanning_tree(graph, cost, parent, processed):
    node = find_lowest_cost_node(cost, processed)
    while node is not None:
        processed.append(node)
        for neighbour in graph[node]:  # 检查node的邻居
            if cost[neighbour] > graph[node][neighbour] and neighbour not in processed:
                cost[neighbour] = graph[node][neighbour]
                parent[neighbour] = node
        node = find_lowest_cost_node(cost, processed)
        

'''按照广度优选原则打印最小生成树'''
def print_best_way(cost, processed):
    for node in processed:
        print('{}--->'.format(node), end='')
    print('\nThe lowest cost is {}'.format(sum(cost.values())))


'''建立无向图'''
def main():
    graph = {}
    graph['v1'] = {}
    graph['v1']['v2'] = 2
    graph['v1']['v3'] = 4
    graph['v1']['v4'] = 1
    graph['v2'] = {}
    graph['v2']['v1'] = 2
    graph['v2']['v4'] = 3
    graph['v2']['v5'] = 10
    graph['v3'] = {}
    graph['v3']['v1'] = 4
    graph['v3']['v4'] = 2
    graph['v3']['v6'] = 5
    graph['v4'] = {}
    graph['v4']['v1'] = 1
    graph['v4']['v2'] = 3
    graph['v4']['v3'] = 2
    graph['v4']['v5'] = 7
    graph['v4']['v6'] = 8
    graph['v4']['v7'] = 4
    graph['v5'] = {}
    graph['v5']['v2'] = 10
    graph['v5']['v4'] = 7
    graph['v5']['v7'] = 6
    graph['v6'] = {}
    graph['v6']['v3'] = 5
    graph['v6']['v4'] = 8
    graph['v6']['v7'] = 1
    graph['v7'] = {}
    graph['v7']['v4'] = 4
    graph['v7']['v5'] = 6
    graph['v7']['v6'] = 1

    infinity = float('inf')
    cost = {}
    for i in range(7):
        cost['v{}'.format(i+1)] = infinity

    parent = {}
    for i in range(7):
        parent['v{}'.format(i+1)] = None

    processed = []
    start = input('enter the start:')
    while start not in graph:
        start = input('not exist!\nenter the start:')
    cost[start] = 0

    build_min_spanning_tree(graph, cost, parent, processed)
    print_best_way(cost, processed)

if __name__ == '__main__':
    main()
