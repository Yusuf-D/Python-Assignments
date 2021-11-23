
def fibonacci(number):
    lst = [1]
    a, b = 0, 1 
    
    while b < number:
        a, b = b, a + b
        lst.append(b)
    return lst

print(fibonacci(55))

