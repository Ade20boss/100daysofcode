print("WELCOME TO THE TIP CALCULATOR")
#collect input of the total bill
bill_without_tip = float(int(input("What was the total bill:$ ")))
#collect the percentage tip
Tip_percent = int(input("What percentage tip would like to give: "))

#calculate the actual amount of the tip
total_tip = (Tip_percent/100)*bill_without_tip
#Add the amount tip gotten to the bill
bill_with_tip = bill_without_tip + total_tip

#ask for the number of people splitting the bill
people = int(input("How many people will be splitting the bill: "))
#divide the total bill(plus tip) by the number of people and round it to 2 decimal places
each_person_payment = round(bill_with_tip/people, 2)

#print answer to the console
print(f"Each person should pay:  ${each_person_payment}")

