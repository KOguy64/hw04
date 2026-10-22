n = int(input("Enter a whole number (0 or greater): "))

sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
    #print(n)

print(f"Digit Sum: {sum}")