class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(2, n//2 + 1):
            if n % i == 0:
                sum += i
        
        if n == 1:
            sum = 1    
        else:
            sum += 1+n
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)