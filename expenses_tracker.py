def total_spent(expenses):
    """Adds up the 'amount' value from every expense dictionary in the list."""
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total


def highest_expense(expenses):
    """Returns the single expense dictionary with the largest amount."""
    if not expenses:
        return None
    return max(expenses, key=lambda e: e["amount"])


def expenses_by_category(expenses, category):
    """Returns a new list containing only expenses matching the given category."""
    matches = []
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            matches.append(expense)
    return matches


def print_expenses(expense_list):
    """Prints a simple formatted line for each expense in the given list."""
    for expense in expense_list:
        print(f"{expense['category']:<15}: {expense['amount']:.2f}")


# ---- Collect expenses from the user ----------------------------------

expenses = []
addmore = "yes"

while True:
    if addmore.lower() != "yes":
        break
    else:
        category = input("Enter expense category: ").strip()

        # Keep asking for amount until it's a valid number
        while True:
            amount_input = input("Enter amount: ").strip()
            try:
                amount = float(amount_input)
                break
            except ValueError:
                print("Invalid amount. Please enter a number (e.g. 45.50).")

        expense = {"category": category, "amount": amount}
        expenses.append(expense)
        addmore = input("Add another expense? (yes/no): ").strip()


# ---- Report ------------------------------------------------------------

print("\n" + "=" * 30)
print("All expenses")
print("=" * 30)
print_expenses(expenses)

print("\n" + "-" * 30)
print(f"Total spent: {total_spent(expenses):.2f}")

top = highest_expense(expenses)
if top:
    print(f"Highest expense: {top['category']} - {top['amount']:.2f}")

print("-" * 30)

view_category = input("\nView expenses for a specific category? (type category name, or press Enter to skip): ").strip()
if view_category:
    filtered = expenses_by_category(expenses, view_category)
    if filtered:
        print(f"\nExpenses in category '{view_category}':")
        print_expenses(filtered)
        print(f"Subtotal for {view_category}: {total_spent(filtered):.2f}")
    else:
        print(f"No expenses found in category '{view_category}'.")