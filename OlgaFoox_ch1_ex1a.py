def sell_tickets():
    total_tickets = 20
    total_buyers = 0

    while total_tickets > 0:
        # Asking user for the desired number of tickets
        try:
            desired_tickets = int(input(f"Enter the number of tickets you want (max 4, remaining: {total_tickets}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Checking if the input is valid
        if desired_tickets < 1 or desired_tickets > 4:
            print("You can buy between 1 and 4 tickets only.")
            continue

        # Checking if enough tickets are available
        if desired_tickets > total_tickets:
            print("Not enough tickets available. Please enter a lower number.")
            continue

        # Updating tickets and the buyer count
        total_tickets -= desired_tickets
        total_buyers += 1

        # Displaying remaining tickets
        print(f"You have purchased {desired_tickets} ticket(s).")
        print(f"Remaining tickets: {total_tickets}")

    #  Displaying total buyers
    print(f"All tickets have been sold. Total number of buyers: {total_buyers}")

# Running the ticket selling function
if __name__ == "__main__":
    sell_tickets()
