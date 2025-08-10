expenses = []

while True:
    choice = input("Add expense (a), View expenses (v), or Quit (q): ").lower()
    if choice == 'a':
        item = input("Enter item: ")
        cost = float(input("Enter cost: "))
        expenses.append((item, cost))
    elif choice == 'v':
        total = 0
        print("\nYour Expenses:")
        for item, cost in expenses:
            print(f"{item}: ₹{cost}")
            total += cost
        print(f"Total: ₹{total}\n")
    elif choice == 'q':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")