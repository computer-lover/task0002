class BMI:
    def __init__(self,weight,height):
        self.weight=weight
        self.height=height
    def BMI(self):
        return self.weight/self.height**2

tb=BMI(60,1.7)
print(tb.BMI())
