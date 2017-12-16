# 这里讨论最长公共子序列问题，非最长公共子串

def max(num1, num2):
    '''返回参数中较大的那一个'''
    if num1 > num2:
        return num1
    else:
        return num2


def dynamic(str1, str2):
    '''动态规划方法解决LCS问题'''
    # 检查参数类型是否正确
    assert type(str1) == str and type(str2) == str, 'wrong type!'

    # 构建动态规划的表格
    table = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]

    # 进行动态规划
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    # 找到其中一个最长公共子序列
    result = []
    i = len(str2)
    j = len(str1)
    while table[i][j] != 0:
        if str2[i-1] == str1[j-1]:
            result.append(str2[i-1])
            i -= 1
            j -= 1
        else:
            if table[i-1][j] > table[i][j-1]:
                i -= 1
            else:
                j -= 1
    result.reverse()

    return table[-1][-1], result


def main():
    str1 = input('Please enter the 1st string: ')
    str2 = input('Please enter the 2nd string: ')

    length, result = dynamic(str1, str2)
    print('LCS\' length: {}'.format(length))
    print('LCS: {}'.format(''.join(result)))

if __name__ == '__main__':
    main()