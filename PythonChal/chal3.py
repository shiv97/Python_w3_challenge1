def isPowerOfThree(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 3 != 0): 
                return False
            n = n // 3
              
    return True

n=int(input())
if(isPowerOfThree(n)): 
    print('Yes') 
else: 
    print('No') 
 