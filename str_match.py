import random
import string


def simple_match(target, pattern):
    assert type(target) is str and type(pattern) is str, 'wrong type'
    target_len = len(target)
    pattern_len = len(pattern)

    for i in range(target_len-pattern_len+1):
        position = i
        for j in range(pattern_len):
            if target[i+j] != pattern[j]:
                position = -1
                break
        if position >= 0: # 找到了对应子串
            return position+1


def build_next_list(pattern):
    assert type(pattern) is str, 'wrong type'
    next = [-1, 0]
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[next[i]]:
            next.append(next[i]+1)
        else:
            index = next[i]
            while index != 0: # 不断分割，尝试匹配
                if pattern[i] == pattern[next[index]]:
                    next.append(next[index]+1)
                    break
                else:
                    index = next[index]
            if index == 0: # 已没有能匹配的部分
                next.append(0)
    return next


def KMP(target, pattern):
    assert type(target) is str and type(pattern) is str, 'wrong type'
    next = build_next_list(pattern) # 构建next数组
    index = j = 0
    while len(pattern)+index <= len(target):
        for i in range(j, len(pattern)):
            if pattern[i] != target[index+i]:
                index += i - next[i]
                j = next[i]
                if j < 0:
                    j = 0
                break
            if len(pattern) == i+1:
                return index+1    
    return None


def main():
    for i in range(10000):
        target = ''.join(random.sample(string.ascii_letters + string.digits, 40))
        pattern = ''.join(random.sample(string.ascii_letters + string.digits, 2))
        ans1 = simple_match(target, pattern)
        ans2 = KMP(target, pattern)
        if ans1 != ans2:
            print('target string: {}'.format(target))
            print('pattern string: {}'.format(pattern))
            print('simple_match: {}'.format(ans1))
            print('KMP: {}'.format(ans2))

if __name__ == '__main__':
    main()  