def can_divide_watermelon(w):
    for i in range(2, w, 2):

        if (w - i) % 2 == 0:
            return "Yes"
    return "No"


w = int(input())

print(can_divide_watermelon(w))
