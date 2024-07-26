def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a = 4
b = 6
print("LCM is:", lcm(a, b))
