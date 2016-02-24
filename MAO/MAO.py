L = [7,2,3,5,0] 


#question, given a list- return a list with the elements updated
#as the product of all the numbers to it's right and left (not including itself)

def MAO(L):
   
    totalProduct = 1
    for num in L:
        totalProduct *= num 

    return [totalProduct//num for num in L if num != 0] #handles 0 case

if __name__ == '__main__':
   print(MAO(L)) 
