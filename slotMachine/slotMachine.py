import random

def spin_row():
    symbols = ['🍆', '🍑']
    return [random.choice(symbols) for _ in range(3)]
    
def print_row(symbolList):
    
    print("\n======SLOT MACHINE======\n")
    
    print(f"{" | ".join(symbolList) :^22}")

    print("\n========================\n")

def get_payout(balance):
    print(f"${balance} has been added to your tab.")

def main():
    balance = 100
    isPlaying = True
    while isPlaying:
        print("\n======SLOT MACHINE======\n")
        print(
            "1. Bet\n2. Balance\n3. Payout\n4. Exit"
        )
        response = input ("\n>>> ").strip().lower()
        print("\n========================\n")

        
        if response == 'bet':
            while True:
                bet = (input("Amount (q to exit): "))
                
                if bet == "q":
                    break

                try:
                    bet = int (bet)
                except ValueError:
                    print("\nEnter Valid Value!\n") 
                    continue

                if bet > balance:
                    print("\nInsufficient Balance\n")
                    continue
                
                elif bet <= 0:
                    print("\nBet can't be negative or zero\n")
                    continue

                else:
                    results = (spin_row())
                    print_row(results)

                    wonOrLose = True
                    for result in results:
                        if result != results[1]:
                            wonOrLose = False
                            break

                    if wonOrLose:
                        print("=====🎉 You  Won 🎉=+===")
                        balance += 3 * bet
                    else:
                        print("you lost.")
                        balance -= bet
                    break
        elif response == "exit":
            isPlaying = False 
            break

        elif response == "balance":
            print(f"Your Balance is: {balance}")
        
        elif response == "payout":
            get_payout(balance)
            isPlaying = False
            continue

        else:
            print("Invalid Input!")



if __name__ == "__main__":
    main()
