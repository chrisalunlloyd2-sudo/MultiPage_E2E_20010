python
# Python Inventory Management System

# Define the main functionality of the project
def manage_inventory():
    # List of items to be added, updated, and removed from inventory
    add_items = ["App", "Computer", "Laptop", "Mouse"]
    update_items = ["New App", "Book", "Notebook", "Pen"]
    remove_items = ["Pencil", "Calculator"]

    print("Inventory Management System")

    # Add items to the inventory
    for item in add_items:
        print(f"Adding: {item}")

    # Update items in the inventory
    update_status = []
    for item in update_items:
        if item not in update_status:
            update_status.append(item)
            print(f"Updating: {item}")
    
    # Remove items from the inventory
    remove_from_list = []
    for item in remove_items:
        if item not in update_status and item not in add_items and item not in remove_status:
            remove_from_list.append(item)
            print(f"Removing: {item}")

    return manage_inventory, add_items, update_items, remove_items, remove_from_list

# Main function
if __name__ == "__main__":
    manage_inventory()