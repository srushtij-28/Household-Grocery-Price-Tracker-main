from config import GROCERIES_FILE, PRICES_FILE
from storage import load_data, save_data
from utils import get_next_id, get_today, get_valid_amount, print_line


def add_price():
    groceries = load_data(GROCERIES_FILE)
    prices = load_data(PRICES_FILE)

    if not groceries:
        print("Add grocery items first.")
        return

    print("\nAvailable groceries:")

    for item in groceries:
        print(f"{item['id']}. {item['name']} ({item['unit']})")

    try:
        grocery_id = int(input("\nEnter grocery ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    grocery = next(
        (item for item in groceries if item["id"] == grocery_id),
        None
    )

    if grocery is None:
        print("Grocery not found.")
        return

    shop = input("Enter shop name: ").strip()

    if not shop:
        print("Shop name is required.")
        return

    price = get_valid_amount("Enter price: ₹")

    record = {
        "id": get_next_id(prices),
        "grocery_id": grocery_id,
        "shop": shop,
        "price": price,
        "date": get_today()
    }

    prices.append(record)
    save_data(PRICES_FILE, prices)

    print("Price recorded successfully!")


def view_prices():
    groceries = load_data(GROCERIES_FILE)
    prices = load_data(PRICES_FILE)

    print_line()
    print("GROCERY PRICE HISTORY")
    print_line()

    if not prices:
        print("No price records found.")
        return

    grocery_map = {
        item["id"]: item["name"]
        for item in groceries
    }

    for record in prices:
        name = grocery_map.get(
            record["grocery_id"],
            "Deleted grocery"
        )

        print(
            f"Item: {name} | "
            f"Shop: {record['shop']} | "
            f"Price: ₹{record['price']:.2f} | "
            f"Date: {record['date']}"
        )


def compare_prices():
    groceries = load_data(GROCERIES_FILE)
    prices = load_data(PRICES_FILE)

    if not groceries:
        print("No grocery items available.")
        return

    print("\nAvailable groceries:")

    for item in groceries:
        print(f"{item['id']}. {item['name']}")

    try:
        grocery_id = int(input("\nEnter grocery ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    grocery = next(
        (item for item in groceries if item["id"] == grocery_id),
        None
    )

    if grocery is None:
        print("Grocery not found.")
        return

    matching = [
        record for record in prices
        if record["grocery_id"] == grocery_id
    ]

    if not matching:
        print("No price records for this item.")
        return

    # Keep the latest recorded price for each shop.
    latest_prices = {}

    for record in matching:
        shop = record["shop"].lower()

        if (
            shop not in latest_prices
            or (record["date"], record["id"])
            > (
                latest_prices[shop]["date"],
                latest_prices[shop]["id"]
            )
        ):
            latest_prices[shop] = record

    print(f"\nPrice comparison: {grocery['name']}")
    print_line()

    sorted_prices = sorted(
        latest_prices.values(),
        key=lambda record: record["price"]
    )

    for record in sorted_prices:
        print(
            f"{record['shop']} - "
            f"₹{record['price']:.2f} "
            f"({record['date']})"
        )

    cheapest = sorted_prices[0]

    print_line()
    print(
        f"Cheapest shop: {cheapest['shop']} "
        f"- ₹{cheapest['price']:.2f}"
    )


def calculate_shopping_cost():
    groceries = load_data(GROCERIES_FILE)
    prices = load_data(PRICES_FILE)

    if not groceries:
        print("No grocery items available.")
        return

    total = 0

    print("\nSHOPPING COST ESTIMATE")
    print_line()

    for grocery in groceries:
        matching = [
            record for record in prices
            if record["grocery_id"] == grocery["id"]
        ]

        if not matching:
            continue

        latest = max(
            matching,
            key=lambda record: (record["date"], record["id"])
        )

        print(
            f"{grocery['name']}: "
            f"₹{latest['price']:.2f} per {grocery['unit']}"
        )

        total += latest["price"]

    print_line()
    print(f"Estimated total: ₹{total:.2f}")
    print("(One unit of each item with a recorded price.)")
