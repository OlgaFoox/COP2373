from functools import reduce

#Asks the user for their expenses and returns a list of dictionaries
def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter expense type (or '1' to finish): ")
        if expense_type == '1':
            break
        amount = float(input("Enter expense amount: "))
        expenses.append({"type": expense_type, "amount": amount})
    return expenses


#Calculates the total expenses w/reduce
def calculate_total(expenses):
    return reduce(lambda total, expense: total + expense["amount"], expenses, 0)


#Finds the highest expense w/reduce
def find_highest_expense(expenses):
    return reduce(lambda highest, expense: expense if expense["amount"] > highest["amount"] else highest, expenses)


#Finds the lowest expense w/reduce
def find_lowest_expense(expenses):
    return reduce(lambda lowest, expense: expense if expense["amount"] < lowest["amount"] else lowest, expenses)


if __name__ == "__main__":
    expenses = get_expenses()

    total_expenses = calculate_total(expenses)
    highest_expense = find_highest_expense(expenses)
    lowest_expense = find_lowest_expense(expenses)

    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Highest expense: {highest_expense['type']} - ${highest_expense['amount']:.2f}")
    print(f"Lowest expense: {lowest_expense['type']} - ${lowest_expense['amount']:.2f}")
