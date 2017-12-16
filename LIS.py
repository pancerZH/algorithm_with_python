def dynamic_On2(str1):
    '''使用动态规划的方法找到最长上升子序列，时间复杂度为O(n^2)'''
    # 检查参数类型
    assert type(str1) == str, 'wrong type!'

    # 构建动态规划表格
    table = [0 for i in range(len(str1))]
    table[0] = 1

    # 进行动态规划
    for i in range(1, len(str1)):
        max_length = 0
        for j in range(len(table)):
            if str1[i] > str1[j] and table[j] > max_length:
                max_length = table[j]
        table[i] = max_length + 1
    
    # 找到最长上升子序列的长度
    max_length = 0
    for i in table:
        if i > max_length:
            max_length = i
    
    # 找到最长上升子序列
    result = []
    length = max_length
    for i in range(len(str1)-1, -1, -1):
        if table[i] == length:
            result.append(str1[i])
            length -= 1
    result.reverse()

    return max_length, result


def main():
    str1 = input('Please enter the string: ')

    max_length, result = dynamic_On2(str1)
    print('LIS\' length: {}'.format(max_length))
    print('LIS: {}'.format(''.join(result)))

if __name__ == '__main__':
    main()