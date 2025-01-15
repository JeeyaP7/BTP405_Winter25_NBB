#code with a specified length of array 
def getficonacci():
    fib = [0, 1]
    while len(fib) < 10:
        fib.append(fib[-1] + fib[-2])
        return fib
    print(fib)
 

 # prof's code 
 # here the sequence is limited to the value 10
def getFibonacciNumbers(n):
    if n < 0:
        return[]
    fib_numbers = [0, 1]
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    return fib_numbers if n >= 1 else [0]

print(getFibonacciNumbers(10))