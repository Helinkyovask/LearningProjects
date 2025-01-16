

def inputValue():
    while True:
        number = input("Enter Number: ")
        try:
            number = int(number)
        except ValueError:
            print("Enter a non-zero positive integer value!")
            continue
        if number == 0:
            print("Enter a non-zero positive integer value!")
            continue
        return number


def checkPrime(number = 1):
    if number == 1:
        print("\n1 is neither prime nor composite.")
    elif number == 2:
        print("\n2 is a prime number.")
    else:
        counter = 2
        for x in range(3, number + 1):
            if number % counter == 0:
                print(f"\n{number} is not a prime number.")    
                break
            counter += 1
        else:
            print(f"{number} is a prime number")


print("\n=====PRIME CHECKER======\n",flush= True)
checkPrime(inputValue())
print("\n========================")
