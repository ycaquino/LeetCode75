'''
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n.

Return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.

Ex. 1
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Ex.2
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''


def can_place_flowers(flowerbed: [int], n: int) -> bool:
    planted = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            continue
        elif i-1 >= 0 and i+1 < len(flowerbed):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                planted += 1
        elif i == 0 and i+1 < len(flowerbed):
            if flowerbed[i+1] == 0:
                flowerbed[i] = 1
                planted += 1
        elif i == len(flowerbed) - 1 and i - 1 >= 0:
            if flowerbed[i-1] == 0:
                flowerbed[i] = 1
                planted += 1
        else:
            flowerbed[i] == 1
            planted += 1
    return planted >= n
