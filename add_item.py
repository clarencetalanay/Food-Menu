def add_menu_item(menu):
    """Adds a new item to the menu, with an option to return to the menu."""
    print("\n--- Add New Menu Item ---")
    print("(Type 'back' at any prompt to cancel)")

    # 1. Get item name
    name = input("Enter item name: ").strip()
    if name.lower() == 'back':
        print("Cancelled. Returning to edit menu...")
        return

    # 2. Get item price
    while True:
        price_input = input("Enter item price: ₱").strip()
        
        if price_input.lower() == 'back':
            print("Cancelled. Returning to edit menu...")
            return

        try:
            price = float(price_input)
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical price or type 'back'.")

    # Auto-generate next sequential ID
    next_id = max(menu.keys(), default=0) + 1
    menu[next_id] = {"name": name, "price": price}
    print(f"Successfully added '{name}' with ID [{next_id}]!")