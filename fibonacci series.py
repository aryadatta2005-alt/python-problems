def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fibonacci(n)