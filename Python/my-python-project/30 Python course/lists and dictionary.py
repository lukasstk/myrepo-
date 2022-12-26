my_cart = [3, 20, 500]
my_cart.append(455)  # adds a value to the list
value_cart = sum(my_cart)  # adds every int in a list
print(value_cart)
print(len(my_cart))  # length of a list
word = "hello world"
print(word[4])
my_items = ["snack", "mouse", "screen", "iphone"]
my_products = [my_items, my_cart]
print(my_products)

# dictionaries
my_data = {"name": "Lukas Stank", "location": "Munich"}
print(my_data.keys())  # prints all keys of my dic
print(my_data["name"])  # prints the value of the key "name"
my_data["occ"] = "Student"  # adds a key-value pair to my dic
print(my_data)
