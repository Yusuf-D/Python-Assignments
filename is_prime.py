def is_prime(n):   
    if n == 2:
        return True
    elif n < 2 or not n % 2:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if not n % i:
                print("It is divisible by", i)
                return False
    return True 

n = int(input("Enter a whole number: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
