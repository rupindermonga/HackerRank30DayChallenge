#Write your code here
class Calculator:
    def power(self,n,p):
        self.n = n
        self.p = p
        if n < 0 or p < 0:
            ans = Exception("n and p should be non-negative")
        else:
            ans = n**p
        return ans

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   