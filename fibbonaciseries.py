def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    
    s = [0, 1]

  
    for i in range(2, n):
        next_number = s[-1] + s[-2]
        s.append(next_number)

    return s


n = int(input("Enter the number of Fibonacci numbers to generate: "))


s = fibonacci(n)


print("The first", n, "numbers in the Fibonacci series are:", s)
