def fibonacci_list(n):
    # Base Cases
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n ==2:
        return [0,1]
    else:
        # Recursive Case: get the list up to n-1 and then append the next Fibonacci number
        fib_seq = fibonacci_list(n - 1)
        next_fib = fib_seq[-1] + fib_seq[-2]  # Calculate the next Fibonacci number
        fib_seq.append(next_fib)  # Append the next number to the list
        return fib_seq
        
x=fibonacci_list(5)
print(x)