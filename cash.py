from cs50 import get_float
m = -1

while m < 0:
    m = get_float("Change owed \n")

cents = round(m  *100)

c = 0


while (cents > 0.00):
    
    if cents >= 25:
        cents = cents - 25
        c += 1
    
    elif cents >= 10:
        cents = cents - 10
        c += 1
    
    elif cents >= 5.0:
        cents = cents - 5
        c += 1
    
    elif cents >= 1.0:
        cents  = cents - 1
        c += 1

print(c)
print("")