from grocery_manager import (
    add_grocery,
    view_groceries,
    update_grocery,
    delete_grocery
)

from price_manager import (
    add_price,
    view_prices,
    compare_prices,
    calculate_shopping_cost
)


def main():
    while True:
        print("\n======================================")
        print(" HOUSEHOLD GROCERY PRICE TRACKER")
        print("======================================")

        print("1. Add Grocery")
        print("2. View Groceries")
        print("3. Update Grocery")
        print("4. Delete Grocery")
        print("5. Add Grocery Price")
        print("6. View Price History")
        print("7. Compare Prices")
        print("8. Calculate Shopping Cost")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_grocery()

        elif choice == "2":
            view_groceries()

        elif choice == "3":
            update_grocery()

        elif choice == "4":
            delete_grocery()

        elif choice == "5":
            add_price()

        elif choice == "6":
            view_prices()

        elif choice == "7":
            compare_prices()

        elif choice == "8":
            calculate_shopping_cost()

        elif choice == "9":
            print("Thank you for using Grocery Price Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
