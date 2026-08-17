from view_menu import display_menu

def reindex_menu(menu):
    items = list(menu.values())
    menu.clear()
    for index, item in enumerate(items, start=1):
        menu[index] = item

def delete_menu_item(menu):
    print("\n--- Delete Menu Item ---")
    if not menu:
        print("The menu is empty. Nothing to delete.")
        return

    display_menu(menu)

    print("(Type 'back' or '0' to cancel)")
    
    while True:
        user_input = input("Enter the ID of the item to delete: ").strip()

        if user_input.lower() == 'back' or user_input == '0':
            print("Cancelled. Returning to edit menu...")
            return

        try:
            item_id = int(user_input)
            if item_id in menu:
                removed = menu.pop(item_id)
                reindex_menu(menu)
                print(f"Successfully removed '{removed['name']}'. Menu IDs updated!")
                break
            else:
                print("Item ID not found. Please try again or type 'back'.")
        except ValueError:
            print("Invalid input. Please enter a numerical ID or type 'back'.")