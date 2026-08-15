def add_food()
name = input("Enter the name of the food you want to add: ")
if not name: 
    print("The food name cant be empty.")
return
if name in menu: 
    print(f"'{name}' is already in the menu.")
    return

try: 
 price = float(input(f"price for the'{name}: $"))
 except ValueError:
    print("invalid product price.")
    return
    menu[name]=price
    print(f"Added '{name}' (${price.2f}) to the menu.")

    def delete_food()

    

