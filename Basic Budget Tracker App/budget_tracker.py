import tabulate
import os
import json

print("""
    _‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗_
    |                                               |
        Welcome to the Budget Tracker Application.
    |_______________________________________________|
      
    """)

# 1. Function to ask for the budget
def set_budget():
    while True:
        budget = input("Set the budget amount: ₹ ")

        if budget.isdigit():
            # print(f"Budget is set to: ₹{budget}")
            break
        else:
            print("Invalid input.\nEnter a valid amount.\n")
        
    return int(budget)


# 2. Function to add expense amount and item
def add_expense(budget, expenses_list):
    new_expense_name = input("Enter the expense item: ").upper()
    new_expense_amount = int(input("Enter expense amount: ₹ "))
    expense = total_expense(expenses_list) + new_expense_amount
    if (expense) > budget:
        print("Cannot add expense.\nYour expense has exceeded the budget.")
    else:
        expenses_list.append([new_expense_name, new_expense_amount])
        print(f"EXPENSE OF ₹{new_expense_amount}/- ON {new_expense_name} ADDED.")
        if budget - expense < 50 and budget > 50:   # Show the warning when budget remaining is below ₹ 50/-
            print(f"WARNING: Budget about to be exceeded.\nRemaing budget is = ₹ {budget - total_expense(expenses_list)}/-\n")


# 3. Function to remove item and corresponding expense amount.
def remove_expense(expenses_list):
    expense_found = False
    expense_to_remove = input("Enter expense name to remove: ").lower()
    
    for i in expenses_list:
        if expense_to_remove == i[0].lower():
            expenses_list.remove(i)
            print(f"EXPENSE OF ₹{i[1]}/- ON {i[0]} REMOVED\n")
            expense_found = True
            break
    if expense_found == False:
        print(f"Error. {expense_to_remove} is not in the list of expenses.\n")


# 4. Function to display expenses and remaining budget
#     Show warning if budget exceeded or about to be exceeded.
def display_expenses(budget, expenses_list):

    if len(expenses_list) == 0:
        print("No expense to display. You have not added any expense.\nPlease add an expense first.")
    else:
        print(f"Budget: {budget}")
        print(tabulate.tabulate(expenses_list, headers=["ITEM PURCHASED", "AMOUNT SPENT (₹)"], tablefmt="grid", numalign="center"))
        print(f"\nTotal amount spent = ₹ {total_expense(expenses_list)}/-")
        print(f"Remaing budget is = ₹ {budget - total_expense(expenses_list)}/-\n")
    

# 5. Function to calculate total expense:
def total_expense(expenses_list):
    total  = 0
    for i in expenses_list:
        total += i[1]
    return total


def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, [] 


def save_budget_details(filepath, budget, expenses_list):
    data = {
        'budget' : budget,
        'expenses' : expenses_list,
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def clear_expenses(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
    
        data['expenses'] = []

        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        
    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError as e:
        print(e)


# The 'main' function to interact with the user.
def main():
    budget = 0

    filepath = 'budget_data.json'

    expenses_list = [] # A list of all the expenses and their cost added by the user.
    budget, expenses_list = load_budget_data(filepath)

    while True:
        try:
            user_choice = int(input("""
                    Menu:
                    1. SET budget.
                    2. CHANGE budget amount.
                    3. ADD a new expense.
                    4. REMOVE an expense.
                    5. SHOW all the expenses.
                    6. CLEAR all expenses.
                    7. EXIT
                    What do you want to do?
                    Select an option number: """))
            print()
        
            if user_choice == 1:
                print("SET BUDGET")
                budget = set_budget()
                print(f"BUDGET SET TO: ₹ {budget}/-\n")

            elif user_choice == 2:
                print("CHANGE THE BUDGET")
                budget = set_budget()
                print(f"NEW BUDGET IS: ₹ {budget}/-\n")

            elif user_choice == 3:
                if budget == 0:
                    print("Please set a budget first.")
                else:
                    print("ADDING AN EXPENSE")

                    add_expense(budget, expenses_list)


            elif user_choice == 4:

                if len(expenses_list) == 0:
                    print("There are no expenses to remove.\nPlease add expenses first.")
                else:
                    print("REMOVING AN EXPENSE")
                    remove_expense(expenses_list)
            
            elif user_choice == 5:
                # for i in range(len(expenses_list)):
                #     print(f"{expenses_list[i][0]}\t{expenses_list[i][1]}\n")
                display_expenses(budget, expenses_list)

            elif user_choice == 6:

                print("Confirmation:")
                clear = input("Do you want to clear all expenses? (y/n) ").lower()
                while True:
                    if clear == 'y':
                        clear_expenses(filepath)
                        expenses_list = []
                        print("All expenses cleared")
                        break
                    elif clear == 'n':
                        print("Ok.")
                        break
                    else:
                        print("Invalid input.\nEnter 'y' for YES or 'n' for NO")

            elif user_choice == 7:
                save_budget_details(filepath, budget, expenses_list)
                print("Application exited.\n\n")
                break
            
            else:
                print("Invalid menu input.\nPlease choose a valid option from the given menu.\n")


        except ValueError as e:
            print(f"Error: Invalid input. Please enter a valid integer.\n{e}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except IndexError as e:
            print(f"Error: {e}\n") 
        except Exception as e:  # Catch any other unexpected exceptions
            print(f"An unexpected error occurred: {e}\n") 


# To run the main function
if __name__ == "__main__":
    main()
