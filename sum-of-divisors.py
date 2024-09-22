"""
Python program to find sum of divisors of a number n,
for example:
print(sum_divisors(0))
# 0
print(sum_divisors(3)) 
# Should sum of 1
# 1
print(sum_divisors(36)) 
# Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) 
# Should be sum of 2+3+6+17+34+51
# 114
 """


def sum_divisors(n):
    divisors = []
    for x in range(1, n):
        if n % x == 0:
            divisors.append(x)
    
    result, divisors = sum_divisors(n)
    print(f"Άθροισμα διαιρετών: {result}")
    print(f"Διαιρέτες: {divisors}")
    return sum(divisors), divisors




