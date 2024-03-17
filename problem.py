def calculate_snacks(budget):
    chip_price = 3.50  # Price of one bag of chips
    soda_price = 1.75  # Price of one bottle of soda

    # Calculate maximum number of bags of chips
    max_chips = budget // chip_price

    # Calculate maximum number of bottles of soda
    max_soda = budget // soda_price

    # Initialize variables to store optimal quantities
    optimal_chips = 0
    optimal_soda = 0
    max_total = 0

    # Iterate over possible combinations of chips and soda within budget
    for chips_count in range(max_chips + 1):
        for soda_count in range(max_soda + 1):
            total_cost = chips_count * chip_price + soda_count * soda_price

            # Update optimal quantities if total cost is within budget and higher than current maximum
            if total_cost <= budget and total_cost > max_total:
                max_total = total_cost
                optimal_chips = chips_count
                optimal_soda = soda_count

    return optimal_chips, optimal_soda

# Input budget from the user
budget = float(input("Enter your budget for snacks: $"))

# Call the function to calculate optimal quantities
optimal_chips, optimal_soda = calculate_snacks(budget)

# Display the results
print("With a budget of $%.2f, you can buy %d bags of chips and %d bottles of soda." % (budget, optimal_chips, optimal_soda))
