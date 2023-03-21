print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_perc = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) /100 + 1
split = int(input("How many people to split the bill? "))

bill_to_pay = (bill * tip_perc) /split
round_bill = round(bill_to_pay, 2)

print(f"Each person should pay: ${round_bill}")