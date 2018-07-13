import random
x=random.randint(100,999)
print("The randomly generated number is",x)
y=str(x)
if y[-1]=='4':
    print("Yes, the random no.",x,"contains 4 at the units place.")
else:
    print("No, the random no.",x,"doesn't contain 4 at the units place.")
'''import random
x=random.randint(100,999)
print("The randomly generated number is",x)
if x%10==4:
    print("Yes, the random no.",x,"contains 4 at the units place.")
else:
    print("No, the random no.",x,"doesn't contain 4 at the units place.")'''

