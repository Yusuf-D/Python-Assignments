
def is_prime(n):
    if n == 2:
        return True
    elif n < 0 or not n % 2:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if not n % i:
                return False
    return True

prime_list = []
number = int(input("Enter a positive whole number: "))

for i in range(2, number+1):
    if is_prime(i):
        prime_list.append(i)

print(prime_list)




