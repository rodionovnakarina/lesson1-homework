class Calculator:

    def sum(a, b):
        result = a+b
        return result

def sum(a, b):
        result = a-b
        return result

def mul(a, b):
        result = a∗b
        
def div(a, b):
        if (b == 0):
        raise ArithmeticError("на ноль делить нельзя")

         return a/b  

def pow(self, a, b=2): 
         return a**b

         def avg(self, nums):
		s = 0

		for num in nums: 
			s = s + num

            l = len(nums)
    return self.div(s, l)