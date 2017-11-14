def move(origin, middle, destination, left_num):
    if left_num == 0:
        return
    move(origin, destination, middle, left_num-1)
    print('move {} from {} to {}'.format(left_num, origin, destination))
    move(middle, origin, destination, left_num-1)

move('A', 'B', 'C', 10)
