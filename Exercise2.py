def printFibonacci(num):
    first=0
    second=1
    fibonacciList =[0,1]
    for x in range(2,num):
        sum = fibonacciList[x-1] + fibonacciList[x-2]
        fibonacciList.append(sum)
    print(*fibonacciList, sep = "\n")

printFibonacci(13)
