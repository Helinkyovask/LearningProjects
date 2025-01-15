from time import sleep

#elements of fib series... number = number of fibb numbers required
fib_series = [1,1,2]
x1 = 1
x2 = 1
x3 = 2
number = 450


#run it for ASMR
print("============")
for _ in range(4,number + 1):
    x1 = x2
    x2 = x3
    x3 = x1 + x2
    print(x3)
    fib_series.append(x3)
    sleep(0.01)
print("====================================================================")


#storing numbers in a file
with open("fibonacciNumbers.txt","w") as f:
    for fib in fib_series:
        f.write(f"{fib}")
        f.write("\n")

