menu = {
    1: {"name": "Fried Chicken", "price": 80},
    2: {"name": "Pancit Canton", "price": 35},
    3: {"name": "Siopao", "price": 50},
    4: {"name": "Burger", "price": 55}
}

def display_menu(menu_data=None):
    """Displays current menu items."""
    if menu_data is None:
        menu_data = menu

    print("\n--- Current Menu ---")
    if not menu_data:
        print("The menu is currently empty.")
    else:
        for item_id, details in menu_data.items():
            print(f"[{item_id}] {details['name']} - ₱{details['price']}")
    print("--------------------")