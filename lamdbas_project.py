#lambda average
average = lambda x, y, z: (x+y+z)/3
print(average(1,2,3))

#lambda max  
Max = lambda x, y: max(x,y)
print(Max(1,2))

#lambda even 
even = lambda x: (x%2)==0 
print(even(2))

cars = {"Bronco": 18.7,
        "Tacoma": 21,
        "Wrangler": 15,
        "F-350": 2}

#sorting cars
print(dict(sorted(cars.items(), key = lambda item: item[1])))


states = [
    {'state': 'Pennsylvania', 'abbreviation':'PA' , 'population': 12800000},
    {'state': 'New Jersey', 'abbreviation': 'NJ', 'population': 8882000},
    {'state': 'Maryland', 'abbreviation': 'MD', 'population': 6046000}
]

#sorting states (abbreviation)
print(sorted(states, key = lambda abbreviations: abbreviations['abbreviation']))

#sorting states (length of name)
print(sorted(states, key = lambda length: len(length['state']), reverse = True))

stateTwo = [ ('Pennsylvania', 'PA', 12800000),
             ('New Jersey', 'NJ', 888200),
             ('Maryland', 'MD', 604600),]
#sorting states (tuple) 
print(sorted(stateTwo, key = lambda pop: pop[2]))

