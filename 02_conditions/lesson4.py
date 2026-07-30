#Assign
ini_amount = 5000

#Ask to user
amount = float(input("How much you want to withdraw? "))

#Check 
if amount <= ini_amount:
    print(f"Withdrawal successful.\nRemaining balance: {ini_amount-amount}")
else:
    print("Insufficent balance.")