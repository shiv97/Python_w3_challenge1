import math

num = int(input("Enter the Number"))

ro = math.sqrt(num)
if int(ro) ** 2 == num:
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")