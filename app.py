numbers = [1,2,3,4,5,6,7,8,9.10]

def addNums(numbers):
    
    sum = 0
    for i in numbers:
        sum += numbers[i]

    return sum

def multiplyNums(numbers):
    multiTotal = 0
    for i in numbers: 
        multiTotal *= numbers[i]

    return multiTotal
