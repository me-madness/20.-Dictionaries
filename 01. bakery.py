# first task from the lecture

data = input().split()

stock = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i + 1]
    stock[food] = quantity
    
print(stock)    
# Second task from me

