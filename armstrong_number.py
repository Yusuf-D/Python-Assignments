

num = input("Enter a whole and positive number: ")
total = 0

if not num.isdigit() or float(num) < 0:
    print( "It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    for i in num:
        total += int(i)**(len(num))

    if total == int(num):
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")