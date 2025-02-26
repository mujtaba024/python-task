number =int(input("Enter a Number:"))

if number > 1:
    is_prime = True

    for i in range(2,number):
        if number % i == 0:
            is_prime =False
            break

    if is_prime:
        print("Yes, It's a Prime Number!")
    else:
        print("No, It's Not a Prime Number!")
else:
    print("No It's Not a Prime Number!")