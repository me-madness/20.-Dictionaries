# first task from the lecture

products_information = input().split()

stock_date = {}

for i in range(o, len(products_information), 2):
    product = products_information[i]
    quantity = products_information[i + 1]
    stock_date[product] = quantity
    
product_search = input().split()

for current_product in product_search:
    if current_product in stock_date:
        print(f"We have {stock_date[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have the product")        

# Second task from me

