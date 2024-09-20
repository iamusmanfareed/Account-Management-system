class User:
    def __init__(self, name, role, company=None):
        self.name = name
        self.role = role
        self.company = company

class Company:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.income = 0
        self.expenses = []
        self.is_expense_approved = False

company_owner = User(name="main_admin", role="main-admin")

def create_company(owner, company_name):
    if owner.role == "owner":
        return Company(name=company_name, owner=owner)
    return None

def permission_access(user, company):
    if user.role == "main-admin":
        return True
    if user.role == "owner":
        return user == company.owner
    if user.role in ["admin", "user"]:
        return user.company == company
    return False

def add_income(admin, company, amount):
    if admin.role == "admin" and admin.company == company:
        company.income += amount
        return True
    return False

def submit_expense(user, company, amount):
    if user.role == "user" and user.company == company:
        company.expenses.append(amount)
        return True
    return False

def approve_expense(admin, company):
    if admin.role == "admin" and admin.company == company:
        company.is_expense_approved = True
        return True
    return False

def view_report(user, company):
    if user.role in ["owner", "main-admin"] or (user.role == "admin" and user.company == company):
        return {
            "Income": company.income,
            "Expenses": company.expenses,
            "Expense Approved": company.is_expense_approved
        }
    return None

def main():
    companies = {}
    users = {}
    while True:
        print('1. Create Company (Owner Only)')
        print('2. Add Income (Admin Only)')
        print('3. Submit Expense (User Only)')
        print('4. Approve Expense (Admin Only)')
        print('5. View Report (Owner, Admin, Main Admin)')
        print('6. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            owner_name = input('Enter your name: ')
            company_name = input('Enter the company name: ')
            owner = User(name=owner_name, role="owner")
            new_company = create_company(owner, company_name)
            if new_company:
                companies[company_name] = new_company
                users[owner_name] = owner
                owner.company = new_company
                print(f"Company '{company_name}' created successfully!")
            else:
                print("Only owners can create a company!")

        elif choice == '2':
            admin_name = input('Enter your name: ')
            company_name = input('Enter company name: ')
            if admin_name in users and company_name in companies:
                admin = users[admin_name]
                company = companies[company_name]
                amount = float(input('Enter income amount: '))
                if add_income(admin, company, amount):
                    print(f"Income of {amount} added to {company_name}!")
                else:
                    print("Only admins can add income for their company.")
            else:
                print("Admin or company not found.")

        elif choice == '3':
            user_name = input('Enter your name: ')
            company_name = input('Enter company name: ')
            if user_name in users and company_name in companies:
                user = users[user_name]
                company = companies[company_name]
                amount = float(input('Enter expense amount: '))
                if submit_expense(user, company, amount):
                    print(f"Expense of {amount} submitted for {company_name}.")
                else:
                    print("Only users can submit expenses for their company.")
            else:
                print("User or company not found.")

        elif choice == '4':
            admin_name = input('Enter your name: ')
            company_name = input('Enter company name: ')
            if admin_name in users and company_name in companies:
                admin = users[admin_name]
                company = companies[company_name]
                if approve_expense(admin, company):
                    print(f"Expenses approved for {company_name}.")
                else:
                    print("Only admins can approve expenses for their company.")
            else:
                print("Admin or company not found.")

        elif choice == '5':
            user_name = input('Enter your name: ')
            company_name = input('Enter company name: ')
            if user_name in users and company_name in companies:
                user = users[user_name]
                company = companies[company_name]
                report = view_report(user, company)
                if report:
                    print(f"Report for {company_name}:")
                    print(f"Income: {report['Income']}")
                    print(f"Expenses: {report['Expenses']}")
                    print(f"Expense Approved: {report['Expense Approved']}")
                else:
                    print("You don't have permission to view the report.")
            else:
                print("User or company not found.")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
