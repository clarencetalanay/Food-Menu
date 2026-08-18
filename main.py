from view_menu import display_menu, menu
from add_item import add_menu_item
from delete_item import delete_menu_item

def edit_menu_submenu(menu):
    """Submenu for editing operations (Add and Delete)."""
    while True:
        print("\n------------------------------")
        print("          EDIT MENU           ")
        print("------------------------------")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Back to Main Menu")
        
        choice = input("Select an option: ").strip()

        if choice == '1':
            add_menu_item(menu)
        elif choice == '2':
            delete_menu_item(menu)
        elif choice == '3':
            print("Returning to main menu...")
            break
        else:
            print("Invalid selection. Please choose between 1 and 3.")

def main():
    while True:
        print("\n==============================")
        print("      KAINAN NI ANGEL MENU     ")
        print("==============================")
        print("1. View Menu")
        print("2. Edit Menu")
        print("3. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            edit_menu_submenu(menu)
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 3.")

if __name__ == "__main__":
    main()