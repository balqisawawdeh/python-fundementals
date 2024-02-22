import unittest

class MathDojo:
    def __init__(self):
        self.result =0

    def add(self, num, *nums):
        self.num=0
        for i in nums:
            self.num+=i
            self.result+=self.num
        return self
    
    def subtract(self, num, *nums):
        self.num=0
        for x in nums:
            self.num+=x
            self.result-=self.num
        return self
    
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

if __name__ == '__main__':
    unittest.main()

