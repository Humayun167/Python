# # def fact(number):
# #     fact = 1
# #     for i in range(1, number):
# #         fact *= i
# #     return fact
# #
# #
# # numbers = int(input("Enter the number: "))
# # factorial = fact(numbers)
# # print(factorial)
#
#
# # def fact(number):
# #     fact = 1
# #     for i in range(1, number):
# #         fact *= i
# #     return fact
# #
# #
# # number = int(input("Enter a Number: "))
# # factorial = fact(number)
# # print("Factorial:", factorial)
#
# def fact(number):
#     fact = 1
#     for i in range(1, number ):  # Adjusted the range to include 'number'
#         fact *= i+ 1
#     return fact
#
#
# number = int(input("Enter a Number: "))
# factorial = fact(number)
# print("Factorial:", factorial)
def fact(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


number = int(input("Enter a Number: "))
factorial = fact(number)
print("Factorial:", factorial)
