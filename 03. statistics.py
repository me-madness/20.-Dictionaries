# first task from the lecture

stock = {}

while True:
    line = input()
    
    if line == "statistics":
        break    

    product, quantity = line.split(": ")
    
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity
        
        
            
            
# Second task from me

