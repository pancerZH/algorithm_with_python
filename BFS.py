from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name, graph_searched):
    search_queue = deque()
    search_queue += graph_searched[name]
    searched = []  # 用于记录已被查找的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print('{} is a mango seller!'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

# 建立图
graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

if not search('you', graph):
    print('no mango seller!')
