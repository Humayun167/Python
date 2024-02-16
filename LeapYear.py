def CheckLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("This is not a leap year")


year = int(input("Enter the year: "))
CheckLeap(year)
