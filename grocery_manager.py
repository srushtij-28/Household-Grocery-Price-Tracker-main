from config import GROCERIES_FILE
from storage import load_data, save_data
from utils import get_next_id, print_line


def add_grocery():
    groceries = load_data(GROCERIES_FILE)

    name = input("Enter grocery name: ").strip()
    unit = input("Enter unit (kg, litre, packet, piece): ").strip()

    if not name or not unit:
        print("Grocery name and unit are required.")
        return

    if any(item["name"].lower() == name.lower() for item in groceries):
        print("This grocery item already exists.")
        return

    grocery = {
        "id": get_next_id(groceries),
        "name": name,
        "unit": unit
    }

    groceries.append(grocery)
    save_data(GROCERIES_FILE, groceries)

    print("Grocery added successfully!")


def view_groceries():
    groceries = load_data(GROCERIES_FILE)

    print_line()
    print("GROCERY LIST")
    print_line()

    if not groceries:
        print("No grocery items found.")
        return

    for item in groceries:
        print(
            f"ID: {item['id']} | "
            f"Name: {item['name']} | "
            f"Unit: {item['unit']}"
        )


def update_grocery():
    groceries = load_data(GROCERIES_FILE)

    try:
        grocery_id = int(input("Enter grocery ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in groceries:
        if item["id"] == grocery_id:
            name = input(
                f"Enter new name [{item['name']}]: "
            ).strip()

            unit = input(
                f"Enter new unit [{item['unit']}]: "
            ).strip()

            if name:
                item["name"] = name

            if unit:
                item["unit"] = unit

            save_data(GROCERIES_FILE, groceries)
            print("Grocery updated successfully!")
            return

    print("Grocery not found.")


def delete_grocery():
    groceries = load_data(GROCERIES_FILE)

    try:
        grocery_id = int(input("Enter grocery ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    updated = [
        item for item in groceries
        if item["id"] != grocery_id
    ]

    if len(updated) == len(groceries):
        print("Grocery not found.")
        return

    save_data(GROCERIES_FILE, updated)
    print("Grocery deleted successfully!")
