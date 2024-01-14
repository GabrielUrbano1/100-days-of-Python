# tip calulator

print("Welcome to the tip calulator")
cost = float(input("Enter the cost of the bill: "))
tip_amount = float(input("Enter the amount to tip: "))
split = int(input("How many people will be splitting the bill: "))

tip_total = float(cost * (tip_amount / 100))

split_total_tip = (tip_total / split)

split_cost_total = float(cost / split)

total = float(split_total_tip + split_cost_total)

total = round(total, 2)

print(f"Each person should pay ${total} per person.")