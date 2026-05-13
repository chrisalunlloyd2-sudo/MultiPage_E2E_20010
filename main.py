def check_data(data):
    if data == "done":
        return True
    else:
        return False

def update_inventory():
    input("Enter inventory details (enter 'done' to exit): ")
    while True:
        if input() == "done":
            break
        else:
            input(f"Enter {input()} and press enter: ")

if __name__ == "__main__":
    main.py  # This should be the script name in Python

    update_inventory()