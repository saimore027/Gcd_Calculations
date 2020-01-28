def gcd(m,n):
    if m < n :
        (m,n)=(n,m)
    if (m%n)==0:
        return n
    else :
        diff = m - n
        return (gcd(max(n,diff),min(n,diff)))
    
                
a=input("Enter 1st Number")
b=input("Enter 2nd Number")
a=int(a)
b=int(b)

print(gcd(a,b))


                
