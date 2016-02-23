def LMD(L):
    index = 0
    leftValue = 0
    rightValue = 0
    min = float('inf')
   
    for number in L:
        rightValue += number

    while index < len(L):
        if abs(leftValue - rightValue) < min:
            min = abs(leftValue - rightValue)

        rightValue -= L[index]
        leftValue += L[index]
        index += 1

    return min

if __name__ == '__main__':
    print(LMD([3,4,2,1])) #should be 4
    print(LMD([1,2,3,4])) #should be 2

