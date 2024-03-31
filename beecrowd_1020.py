days = float(input())

year = days // 365
month = (days % 365) // 30
days = (days % 365) % 30

print("{} ano(s)".format(year))
print("{} mes(es)".format(month))
print("{} dia(s)".format(days))



def calculate_age(age_in_days):
    # Calculate years, months, and days
    years = age_in_days // 365
    months = (age_in_days % 365) // 30
    days = (age_in_days % 365) % 30

    return years, months, days


def print_age_in_years_months_days(years, months, days):
    # Print the result
    print("{} ano(s)".format(years))
    print("{} mes(es)".format(months))
    print("{} dia(s)".format(days))


# Read the input value
age_in_days = int(input("Enter age in days: "))

# Call the function to calculate age
years, months, days = calculate_age(age_in_days)

# Call the function to print age
print_age_in_years_months_days(years, months, days)
