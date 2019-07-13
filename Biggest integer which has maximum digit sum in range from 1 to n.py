def tomsNum(n):
    #Write the code to solve the problem below
    num = int(n)
    
    List = []
    while num > 0:
        List.append(num % 10)
        num = int(num/10)
        
    List.reverse() 
    mySum = sum(List)
    noOfDigits = len(List)
    
    for i in range(1, noOfDigits):
        List[i] = 9
    
    newSum = sum(List)
    output = int("".join(map(str, List)))
    
    if(output > num):
        output = output - 10 ** (noOfDigits - 1)
    
    if(mySum >= (newSum - 1)):
        return n
    else:
        return output


    
n = input()
print(tomsNum(n))
