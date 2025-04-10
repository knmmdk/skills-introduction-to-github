def guess1(n):
    while (n%2==1) and (n!=1):
     n=3*n+1
     print(n)
     if n!=1:
        pass
    return n
def guess2(n):
    while (n%2==0) and (n!=1):
     n=int(n/2)
     print(n)
     if n!=1:
        pass
    return n
n=int(input("original number:"))
while n!=1:
    n = guess1(n)
    n = guess2(n)
print("Now it's 1, game over")

