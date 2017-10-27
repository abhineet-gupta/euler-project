#The function f is defined for all positive integers as follows:

#f(1)=1
#f(3)=3
#f(2n)=f(n)
#f(4n+1)=2f(2n+1)−f(n)
#f(4n+3)=3f(2n+1)−2f(n)
#The function S(n) is defined as ∑ni=1f(i).

#S(8)=22 and S(100)=3604.

#Find S(337). Give the last 9 digits of your answer.

def f(n):
    if n==1:
        return 1
    elif n==3:
        return 3
    elif n%2==0:
        return f(n//2)
    elif (n-1)%4==0:
        temp = (n-1)//4
        return (2 * f(2*temp + 1) - f(temp))
    elif (n-3)%4==0:
        temp = (n-3)//4
        return (3 * f(2*temp + 1) - 2*f(temp))
    
def s(n):
    result = 0
    for i in range(1, n+1):
        result += f(i)
    return result

print (s(pow(3, 37))%1000000000)
#print (s(100))
