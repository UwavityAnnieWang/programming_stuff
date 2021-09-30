
class Term:
    import math 
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
    
    def integration(self):
        new_coeff = self.coefficient/(self.power+1)
        new_pow = self.power + 1
        new_term = Term(new_coeff, new_pow)
        return new_term
    #evaluate term
    def evaluate(self, number):
        import math 
        return self.coefficient*(math.pow(number, self.power))
        
        
    
    
thing = Term(1,1)
print(thing.integration().power)
class Equation:
    def __init__(self, terms):
        self.terms = terms
    def Integrate(self, a, b):
        new_list_1 = [x.integration().evaluate(a) for x in self.terms]
        new_list_2 = [x.integration().evaluate(b) for x in self.terms]
        new_list_3 = [new_list_2[x]-new_list_1[x] for x in range(len(self.terms))]
        return new_list_3
    
    
    def Integrate_Rect(self, a, b, num_rectangles):
        import numpy
        interval = numpy.arange(a, b, ((b-a)/num_rectangles))
        
        list_of_intervals = []
        
        
        for x in self.terms:
            rectangle_sum = 0
            for y in interval:
                
                
                
                rectangle_sum = rectangle_sum + x.evaluate(y)*x.integration().evaluate(y)
            list_of_intervals.append(rectangle_sum)
        return list_of_intervals
                
        
                
            
                
                
            

    
