class MathDojo:
    def init(self):
        self.result = 0
def add(self, num, *nums):
    self.result += num
    for a in nums:
        self.result += a
    return self
def subtract(self, num, *nums):
    self.result -= num
    for s in nums:
        self.result -= s
    return self
md = MathDojo()
  
#x = md.add(2).add(2,5,1).subtract(3,2).result
y = md.add(1,3,8).add(40).add(100).result
#z = md.subtract(1,100,3).subtract(1,99).subtract(50,20).result
print(y)