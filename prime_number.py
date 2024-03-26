# lower = int(input(""))
# upper = int(input(""))
#
# for num in range (lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num%i == 0:
#                 break
#             else:
#                 print(num)

# num = 97
# for i in range(2, num):
#     if num % i == 0:
#         print("This is not prime")
#         break
# else:
#     print("This is prime")
import math


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Example usage:
number = 97
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
