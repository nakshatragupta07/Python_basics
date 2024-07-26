def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == n

print(is_armstrong(153))
print(is_armstrong(123))
