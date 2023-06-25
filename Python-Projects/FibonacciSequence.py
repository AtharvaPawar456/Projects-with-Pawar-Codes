# Fibonacci Sequence 

def fibonacci(n):
    sequence = []
    a, b = 0, 1

    # Generate the Fibonacci sequence up to the 
    # given number of terms (n)
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test the function
num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(num_terms)
print(fib_sequence)

'''
=================================
Test Case:
=================================

Enter the number of terms: 4
[0, 1, 1, 2]

'''