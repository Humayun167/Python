def sum(n):
    return n + n
    numbers = (2, 3, 4, 5, 6)
    result = map(sum, numbers)
    print(list(result))


def check(n):
    if n % 2 == 0:
        return (f'{n} is an even number ')
    else:
        return (f'{n} is a odd number')


l = {i for i in range(1, 21)}
list(map(check, l))
def a(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print("\n")

n = 5
a(n)