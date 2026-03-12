numbers = [1, 2, 3, 4, 5, 6]
result = []

for n in numbers:           # The Loop
    if n % 2 == 0:          # The Filter (Condition)
        result.append(n**2) # The Transform (Expression)
print(result)              # Output: [4, 16, 36]

