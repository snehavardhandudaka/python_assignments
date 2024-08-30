def calculate_change(amount_paid, total_cost):
    change = amount_paid - total_cost
    if change < 0:
        return "Insufficient funds"

    denominations = [50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    change_dict = {}

    for denom in denominations:
        num = int(change // denom)
        if num > 0:
            change_dict[denom] = num
            change -= num * denom

    return change_dict


amount_paid = float(input("Enter the amount paid: "))
total_cost = float(input("Enter the total cost: "))

change_dict = calculate_change(amount_paid, total_cost)
print("Change needed:")
for denom, count in change_dict.items():
    print(f"${denom:.2f}: {count}")
