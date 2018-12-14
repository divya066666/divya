def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=4
b=2
GCD=gcd(a,b)
print(GCD)
