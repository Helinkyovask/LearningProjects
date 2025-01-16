#Customer Data
if __name__ == '__main__':
    customerInfo = {
        "Alice": 1200.50,
        "Bob": 150.75,
        "Charlie": 300.00,
        "Diana": 450.25
    }


def showBalance(customer_name , customers = customerInfo):
    customer_name = customer_name.lower().capitalize()
    if customer_name in customers:
        print(
            "\n============BALANCE=============",
            f"Name: {customer_name}\nBalance: {customers.get(customer_name)}",
            "================================\n",
            sep = '\n'
            )
    else:
        print("\nEnter a valid customer name!")
    

def deposit(customer_name, amount, customers = customerInfo):
    customer_name = customer_name.lower().capitalize()
    try:
        amount = int(amount)
    except ValueError:
        print("\nEnter valid amount!")
        return
    if customer_name in customers:
        customers.update({customer_name : amount + customers.get(customer_name)})
        
        print(
            "\n=====Successful Transaction=====",
            f"Account Holder Name: {customer_name}",
            f"Amount: {amount}",
            f"Transaction Type: Deposit",
            "================================\n",
            sep= "\n"
            )
    else:
        print("\nEnter a valid customer name!")

def withdraw(customer_name, amount , customers = customerInfo):
    customer_name = customer_name.lower().capitalize()
    try:
        amount = int(amount)
    except ValueError:
        print("\nEnter valid amount!")
        return
    if customer_name in customers:
        customers.update({customer_name : customers.get(customer_name) - amount})
        
        print(
            "\n=====Successful Transaction=====",
            f"Account Holder Name: {customer_name}",
            f"Amount: {amount}",
            f"Transaction Type: Withdraw",
            "================================\n",
            sep= "\n"
            )
    else:
        print("\nEnter a valid customer name!")
def main():
    while True:
        name = input ("Name (press 'q' to exit): ").lower().capitalize()
        if name != 'Q':
            while True:
                functionality = input("Functionality:\n(Check Balance | Deposit | Withdraw) ").lower()
                match functionality:
                    case "check balance" | "checkbalance" | "check_balance":
                        showBalance(customer_name= name)
                        break
                    case "deposit":
                        amount = input("Amount: ")
                        deposit(customer_name= name, amount= amount)
                        break
                    case "withdraw":
                        amount = input("Amount: ")
                        withdraw(customer_name= name, amount= amount)
                        break
                    case _:
                        print("Invalid Input!")
        else:
            break

if __name__ == '__main__':
    main()