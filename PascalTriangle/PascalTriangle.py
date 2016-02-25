def pascalTriangle(level): #head recursive 
    if level is 0:
        return []
    elif level is 1:
        return [[1]]

    else:
        triangle = pascalTriangle(level - 1)

        prevRow = triangle[-1] #get last row
        curRow = []
        
        for i in range(0, len(prevRow)):
            if i is 0:
                curRow.append(1)

            else:
                curRow.append(prevRow[i - 1] + prevRow[i])

        curRow.append(1)
       
        triangle.append(curRow)
        return triangle


if __name__ == '__main__':
    print(pascalTriangle(5))
