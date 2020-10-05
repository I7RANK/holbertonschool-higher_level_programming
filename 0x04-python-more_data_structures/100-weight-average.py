#!/usr/bin/python3
def weight_average(my_list=[]):
    average = []
    mul = 1
    sum1 = 0
    sum2 = 0
    if average == my_list:
        return 0
    for i in my_list:
        for j in i:
            mul *= j
        sum2 += j
        average.append(mul)
        mul = 1
    sum1 = sum(average)

    return sum1 / sum2
