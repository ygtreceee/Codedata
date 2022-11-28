"""
#合并列表
def merge(L1, L2):
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1

    if L1[0] > L2[0]:
        return [L1[0]] + merge(L1[1:len(L1)], L2)
    else:
        return [L2[0]] + merge(L1, L2[1:len(L2)])


if __name__ == "__main__":
    X = input("请输入列表X：").split(",")
    Y = input("请输入列表Y：").split(",")
    S = merge(X, Y)
    for i in range(len(S)):
        S[i] = int(S[i])
    print(S)

#汉诺塔
def Hanoi(n, A, C, B):
    global count
    if n < 1:
        print('invalid input')
    elif n == 1:
        count = count + 1
        print("%d:\t%s ---> %s" % (count, A, C))
    else:
        Hanoi(n - 1, A, B, C)
        Hanoi(1, A, C, B)
        Hanoi(n - 1, B, C, A)


if __name__ == "__main__":
    print("请输入A柱子上的圆盘个数:")
    n = int(input())
    count = 0
    Hanoi(n, "A", "C", "B")

#斐波那契数列
def fab(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


if __name__ == "__main__":
    global result
    n_str = input('请输入需要计算fabonacci数列的第几个元素:')
    n = int(n_str)
    result = fab(n)
    print(result)

#欧几里得算法
def assignment(a,dec):
    x = a; y = dec
    while y:
        temp = x
        r = x % y
        x = y
        y = r
    if x != 1:
        print("{}和{}的最大公约数为{}。".format(a, dec, x))
    else:
        print("{}与{}互质。".format(a, dec))


if __name__ == "__main__":
    M = int(input())
    N = int(input())
    x = assignment(M, N)

#冒泡排序
def bubbleSort(a):
    for i in range(len(array), 1, -1):
        for j in range(i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)
    return array


if __name__ == '__main__':
    arraystr = input().split(',')
    array = [int(i) for i in arraystr]
    print("排序之后的结果为：{}".format(bubbleSort(array)))

# 选择排序
arraystr = input().split(',')
array = [int(i) for i in arraystr]


def selectsort(array):
    # ********* Begin *********
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
        print(array)
    # ********* End *********
    return array


print("排序之后的结果为：{}".format(selectsort(array)))

#数值数据表示（一） 基础习题1
from random import *

def dec2bin_Int(dec):
    binum = ''
    x = bin(dec)
    binum = x[2:]
    binum = binum[::-1]
    return binum[::-1]


def dec2bin_Point(dec, length):
    binum = ''
    x = dec
    while x:
        x *= 2
        binum += ('1' if x >= 1. else '0')
        x -= int(x)
    binum = binum[:length]
    return '0.'+binum


def bin2oh(binum, oh):
    result = ''
    if oh == 'o':
        x = oct(int(binum, 2))
        result = x[2:]
        return result
    elif oh == 'h':
        x = hex(int(binum, 2))
        result = x[2:]
        result = result.upper()
        return result


if __name__ == '__main__':
    seed(0)
    tests = [randint(1, n) for n in [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]]
    bins = []
    for num in tests:
        binum = dec2bin_Int(num)
        print(binum)
        bins.append(binum)

    print('*'*30)

    seed(99)
    decimals = []
    for i in range(10):
        decimals.append(round(random(), 3))
    print(decimals)
    for dec in decimals:
        print(dec2bin_Point(dec, 8))

    print('*' * 30)
    print(tests)
    for binum in bins:
        print(bin2oh(binum, 'o'))
    print('*' * 30)
    for binum in bins:
        print(bin2oh(binum, 'h'))

#基础习题(2)
from random import *

def makechange(num):
    changes = {}
    t = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    numint = int(num)
    numdec = round(num - numint, 2)
    for i, money in enumerate(t):
        if numint != 0:
            res = numint // money
        else:
            res = numdec // money
        if i < 6 and res != 0:
            changes[t[i]] = numint // money
            numint = numint % money
        elif i > 5 and res != 0:
            changes[t[i]] = int(numdec // money)
            numdec = round(numdec % money, 2)
    return changes


if __name__ == '__main__':
    seed(0)
    for i in range(10):
        num = round(random() * 100, 2)
        print(sorted(makechange(num).items(), key=lambda item: item[0], reverse=True))

#置换加密
import math

def encryptMessage(key, message):
    if key <= 0:
        return message
    else:
        return "".join([message[i::key] for i in range(key)])

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns

    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns-1 and row >= numOfRows - numOfShadeBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)


if __name__ == '__main__':
    messages = ["Behind every successful man there's a lot of unsuccessful years.",
                'Common sense is not so common.',
                'There are no secrets to success.It is the result of preparation, hard work, and learning from failure.',
                'All things are difficult before they are easy.']
    for message in messages:
        for key in range(8, 10):
            encrytext = encryptMessage(key, message)
            print(encrytext)
            print(decryptMessage(key, encrytext))
"""

