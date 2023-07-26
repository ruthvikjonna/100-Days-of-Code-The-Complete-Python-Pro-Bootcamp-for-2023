print("Welcome to the Tip Calculator!")

total_bill = float(input("What is the total bill?\n$"))
percent_tip = float(input("What percentage tip would you like to give?\n"))
number_split = float(input("How many people will be splitting the bill?\n"))

total_cost = total_bill * (1 + (percent_tip / 100))
split_cost = format(total_cost / number_split, "0.2f")

print("Each person should pay:\n$" + split_cost)
