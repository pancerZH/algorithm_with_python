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


def dynamic_Onlogn(str1):
    '''使用动态规划的方法找到最长上升子序列，时间复杂度为O(nlogn)'''
    # 检查参数类型
    assert type(str1) == str, 'wrong type!'

    # 构建动态规划表格，记录上升序列的最末元素
    table = [0 for i in range(len(str1))]

    # 进行动态规划
    length = 1
    table[0] = str1[0]
    for i in range(1, len(str1)):
        if str1[i] > table[length-1]:
            table[length] = str1[i]
            length += 1
        else: # 执行一个二分查找
            start = 0
            end = length-1
            while end >= start:
                middle = int((start+end) / 2)
                if table[middle] > str1[i] and (middle == 0 or table[middle-1] < str1[i]) :
                    table[middle] = str1[i]
                    break
                else:
                    if table[middle] > str1[i]:
                        end = middle-1
                    else:
                        start = middle+1

    return length


def main():
    str1 = input('Please enter the string: ')

    max_length, result = dynamic_On2(str1)
    print('LIS\' length: {}'.format(max_length))
    print('LIS: {}'.format(''.join(result)))

    max_length2 = dynamic_Onlogn(str1)
    assert max_length == max_length2, 'wrong answer!'

if __name__ == '__main__':
    main()