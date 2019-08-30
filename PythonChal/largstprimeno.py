def largest_prime_factor(num):
    i = 2
    while i * i < num:
        while num % i == 0:
            num = num / i
        i = i + 1
    return num    
n1=int(input('enter no.:'))
print(largest_prime_factor(n1))


