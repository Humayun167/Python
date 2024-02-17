def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        # print("Average is : ", sum / len(numbers))

        return sum / len(numbers)


c = average(5, 4, 3, 3)
print(c)


def name(**name):
    print("Hello", name["fname"], name["mname"], name["mname"])


name(fname="Humayun", mname="Rashid", lname="khan")
