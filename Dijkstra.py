def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost  = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_lowest_weight_way(graph, costs, parent, processed):
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for i in neighbours:
            new_cost = cost + neighbours[i]
            if new_cost < costs[i] and i not in processed:  # ????
                costs[i] = new_cost
                parent[i] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)


def print_best_way(parent, node, start):
    if node == start:
        print('{}--->'.format(node), end='')
        return
    print_best_way(parent, parent[node], start)
    print('{}--->'.format(node), end='')

graph = {}
graph['a'] = {}
graph['a']['b'] = 2
graph['a']['c'] = 5
graph['b'] = {}
graph['b']['c'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['d'] = 2
graph['c']['e'] = 4
graph['d'] = {}
graph['d']['f'] = 1
graph['e'] = {}
graph['e']['d'] = 6
graph['e']['f'] = 3
graph['f'] = {}

infinity = float('inf')
costs = {}
costs['b'] = 2
costs['c'] = 5
costs['d'] = costs['e'] = costs['f'] = infinity

parent = {}
parent['b'] = 'a'
parent['c'] = 'a'
parent['d'] = parent['e'] = parent['f'] = None

processed = []
end = 'f'
start = 'a'

find_lowest_weight_way(graph, costs, parent, processed)
print_best_way(parent, end, start)
print('The lowest cost is {}'.format(costs[end]))
