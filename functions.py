def fibonacci_sequence(n):
    # Initializing the first two terms of the sequence
    fib_sequence = [0, 1]

    # To Generate Fibonacci sequence up to the specified term
    while len(fib_sequence) < n:
        # To Calculate the next term by summing the last two terms
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

def main():
    # To Prompt user to enter the number of terms in the sequence
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    # To generate Fibonacci sequence up to the specified term
    sequence = fibonacci_sequence(n)

    # Expected to display the Fibonacci sequence
    print("Fibonacci sequence up to term", n, ":", sequence)

if __name__ == "__main__":
    main()
