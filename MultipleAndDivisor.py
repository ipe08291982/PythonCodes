
def miltiple(num, num1):
    if num > num1:
        z = num
    else:
        z = num1

    while (True):
        if z%num==0 and z%num1==0:
            lcm=z
            break;
        z += 1
    return lcm

def divisor(num, num1):
    x = []
    i = 1
    j = min(num, num1)
    while i != j:
        if (num % i) == 0 and (num1 % i) == 0:
            x.append(i)
        i += 1
    return max(x)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("The Least common multiple of " + str(a) + " and " + str(b) + " is: ",miltiple(a, b))
print("The Greatest common divisor of " + str(a) + " and " + str(b) + " is: ",divisor(a, b))
