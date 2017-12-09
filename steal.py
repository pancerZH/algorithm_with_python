def steal_what(capacity, money_list, weight_list):
    # 构建背包表格
    tablet = []
    choice = []
    # 第一行作为标识行，不记录商品信息
    tablet = [[0 for i in range(capacity)] for j in range(len(money_list)+1)]
    choice = [[[] for i in range(capacity)] for j in range(len(money_list)+1)]
    
    # 进行动态规划
    row = len(tablet)
    column = len(tablet[0])
    for i in range(1, row):
        for j in range(column):
            # 获取上一行同列商品价格
            front = i-1
            front_money = tablet[front][j]
            # 获取当前商品加除去当前商品占用空间外其余商品的最大价值之和
            sum_money = 0
            left_weight = j+1-weight_list[i-1]
            if left_weight > 0:
                sum_money = money_list[i-1] + tablet[front][left_weight-1]
            elif left_weight == 0:
                sum_money = money_list[i-1]
            # 当前格子价值等于两者价格较大者
            if front_money > sum_money:
                tablet[i][j] = front_money
                choice[i][j] = choice[front][j]
            else:
                tablet[i][j] = sum_money
                if left_weight > 0:
                    choice[i][j] = choice[front][left_weight-1] + [i-1]
                else:
                    choice[i][j] = [i-1]

    return tablet[-1][-1], choice[-1][-1]


def main():
    money_list = [3000, 2000, 1500]
    weight_list = [4, 3, 1]
    capacity = 4
    money, choice_list = steal_what(capacity, money_list, weight_list)
    print('goods_list:{}, most_money:{}'.format(choice_list, money))


if __name__ == '__main__':
    main()