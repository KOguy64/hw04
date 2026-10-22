def contains(num, digit):
    digits = [(num % (10 ** (i + 1))) // (10 ** i) for i in range(len(str(num)))]
    #print(digits)
    return num % digit == 0 or digit in digits

# 100 * a + 10 * b + c

for i in range(1,101):
    msg = ""
    if contains(i, 3):
        msg += "Fizz"
    if contains(i, 5):
        msg += "Buzz"

    print(f"{i} {msg}")
