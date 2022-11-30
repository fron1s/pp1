array = [
    {'country': "Poland, ", "population" : 38000000},
    {'country': "Ukraine, ", "population" : 43000000},
    {'country': "Germany, ", "population" : 83000000},
    {'country': "Italy,  ", "population" : 59000000},
    {'country': "Netherlands,   ", "population" : 17500000},

]
 
i = 0 
while i < len(array):
    for x, y in array[i].items():
        print(x," - ", y, end= " ")
    i = i+1
    print()




