from datetime import date


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def get_valid_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Please enter a valid number.")


def get_today():
    return date.today().isoformat()


def print_line():
    print("-" * 55)
