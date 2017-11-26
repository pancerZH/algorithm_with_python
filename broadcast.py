'''遍历所有广播站，并从中选出所有广播站中覆盖未被覆盖的州数量最多的那个'''
def find_best_solution(states_needed, stations):
    final_stations = set()
    while states_needed:  # 在states_needed被清空前持续循环
        states_covered = set()
        best_station = None
        # station(str)代表广播站，states_of_station(set)是该广播站覆盖的州
        for station, states_of_station in stations.items():
            covered = states_needed & states_of_station  # 找到所有未被覆盖的州
            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station
        states_needed -= states_covered  # 删去已被覆盖的州
        final_stations.add(best_station)
    return final_stations

'''创建广播站集和每个广播站覆盖的州集'''
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = find_best_solution(states_needed, stations)

'''展示使用贪心法找到的广播站'''
print(final_stations)
    