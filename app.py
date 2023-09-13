numbers = [1,2,3,4,5,6,7,8,9.10]

def addNums(numbers):
    
    sum = 0
    for i in numbers:
        sum += i

    print("Sum: " + str(sum))
    return sum

def multiplyNums(numbers):
    multiTotal = 1
    for i in numbers: 
        multiTotal *= i

    print("Product: " + str(multiTotal))
    return multiTotal

def reverseNums(numbers):
    reversed_nums = list(reversed(numbers))

    for i in reversed_nums:
        print(str(i) + " " ,end="")
    return reversed_nums


def main():
    print("stuff")
    numbersstr = input("Type numbers separated by commas ").split(',')
    numbers = []
    for i in numbersstr:
        numbers.append(int(i))

    
    addNums(numbers)
    multiplyNums(numbers)
    reverseNums(numbers)
    
    #I am adding this comment in order to fulfill part 10
    
if __name__ == "__main__": main()

        