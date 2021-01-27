bill = float(input("What is the amount of the bill? £"))
shares = int(input("How many people are sharing the bill? "))
tip = int(input("What percent tip would you like to leave? "))

tip_percent = tip / 100
bill_tip_percent = bill * tip_percent
bill_with_tip = bill + bill_tip_percent
share_of_bill = bill_with_tip / shares
final_amount = round(share_of_bill, 2)

print(f"Each person should pay {final_amount}")
