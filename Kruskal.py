'''使用队列'''
from collections import deque


'''找到某一节点的祖先'''
def find(parent, node):
    father = node
    while parent[father] is not None:
        father = parent[father]
    return father


'''将某节点调整为所在集合的祖先'''
def make_me_ancestor(parent, node):
    father = parent[node]
    me = node
    while father:
        grandfather = parent[father]
        parent[father] = me
        me = father
        father = grandfather
    parent[node] = None


'''连接两个节点'''
def union(father, son, graph, parent):
    make_me_ancestor(parent, son)  # 将son调整为其所在集合的祖先，便于连接
    parent[son] = father


'''找到不会形成圈的最小权值的边'''
def find_min_edge(graph, parent):
    father = son = None
    weight = float('inf')
    for i in graph:
        for j in graph[i]:
            if graph[i][j] < weight and find(parent, i) is not find(parent, j):
                father = i
                son = j
                weight = graph[i][j]
    return father, son


'''建立最小生成树'''
def build_min_spanning_tree(graph, parent):
    father, son = find_min_edge(graph, parent)
    while father is not None:
        union(father, son, graph, parent)
        father, son = find_min_edge(graph, parent)


'''打印最小生成树'''
def print_spanning_tree(graph, parent):
    queue = deque([None])
    cost = 0
    while queue:
        father = queue.popleft()
        for son in parent:
            if parent[son] == father:
                queue.append(son)
                print('{}--->'.format(son), end='')
                if father is not None:
                    cost += graph[father][son]
    print('\nThe lowest cost is {}'.format(cost))


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

    parent = {}
    for i in range(7):
        parent['v{}'.format(i+1)] = None

    build_min_spanning_tree(graph, parent)
    print_spanning_tree(graph, parent)

if __name__ == '__main__':
    main()
