def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average number is: ", sum / len(numbers))


average(4, 3, 43, 4, 4, 6, 4, 35)


def name(**name):
    print("hello,", name["fname"],
          name["mname"], name["lname"])


name(fname="tufayel", mname="Rashid", lname="khan")
