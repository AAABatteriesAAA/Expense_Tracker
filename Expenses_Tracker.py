
class Expense:
    def __init__(self, date, amount, description):
        "Initializes each expense."
        "Precondition: "
        "date is a MM/DD/YYYY format"
        "amount is an int or float amount"

        self.date=date
        self.amount=amount
        self.description=description

class Tracker:
    def __init__(self):
        self.expenses=[]

    def add_expense(self,expense):
        self.expenses.append(expense)

    def remove_expense(self,index):
        if 0<=index<len(self.expenses):
            self.expenses.remove(self.expenses[index-1])
            print("Successfully removed expense! :)")
        print("The expense does not exist. Please try again.")

    def view_expenses(self):
        if len(self.expenses)==0:
            print("Unfortunately, there is no expenses to show. Please add"
            " an expense before being able to see it.")
        else:
            print("Expense List:")
            for idx, expense in enumerate(self.expenses, 1):
                print(f"{idx}. Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}")
    def total_expenses(self):
        total= sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

class UserView():
    tracker=Tracker()

    while True:
        print("\nExpense Tracker Menu: ")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expense")
        print("4. Total Expenses")
        print("5. Exit lol")

        selection= input("Select your choice (1-5): ")

        if selection=="1":
            date= input("Enter the date (MM/DD/YYYY): ")
            amount= float(input("Enter the amount: "))
            description= input("Enter the description: ")
            expense= Expense(date, amount, description)
            tracker.add_expense(expense)
            print("Expense added successfully!!")
        elif selection=="2":
            indexing= int(input("Please select index: "))-1
            tracker.remove_expense(indexing)
        elif selection=="3":
            tracker.view_expenses()
        elif selection=="4":
            tracker.total_expenses()
        elif selection=="5":
            print("Have a nice day!! :)")
            break
        else:
            print("Please try again >:(")
