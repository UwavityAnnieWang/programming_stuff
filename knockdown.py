import random
def knockdown():
    pins_down = 0
    values = {7:2, 8:2, 9:3, 10:4}
    
    for i in range(1, 4):
        pins=random.randint(0,10)
        if(pins in range(4, 7)):
            pins_down = pins_down+1
             
        elif(pins in range(7,11)):
            pins_down = pins_down + values[pins]
        
    if(pins_down==5):
        return True
    else:
        return False
            
             
            
        
           
           
    

print(knockdown())
