import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Usman@123",
    database="account_management_system"
)
cursor = db.cursor()

def create_user(name, role, company_name=None):

    company_id = None
    if company_name:
        cursor.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
        company = cursor.fetchone()
        if company:
            company_id = company[0]
        else:
            print(f"Company '{company_name}' not found.")
            return

    cursor.execute("INSERT INTO users (name, role, company_id) VALUES (%s, %s, %s)", (name, role, company_id))
    db.commit()
    print(f"User '{name}' created successfully.")

def create_company(company_name, owner_name):
    cursor.execute("SELECT id FROM users WHERE name = %s AND role = 'owner'", (owner_name,))
    owner = cursor.fetchone()
    if owner:
        owner_id = owner[0]
        cursor.execute("INSERT INTO companies (name, owner_id) VALUES (%s, %s)", (company_name, owner_id))
        db.commit()
        print(f"Company '{company_name}' created successfully.")
    else:
        print(f"Owner '{owner_name}' not found or not an owner.")

def add_income(admin_name, company_name, amount):
    cursor.execute("SELECT id FROM users WHERE name = %s AND role = 'admin'", (admin_name,))
    admin = cursor.fetchone()
    if admin:
        cursor.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
        company = cursor.fetchone()
        if company:
            company_id = company[0]
            cursor.execute("UPDATE accounts SET income = income + %s WHERE company_id = %s", (amount, company_id))
            db.commit()
            print(f"Income of {amount} added to {company_name}.")
        else:
            print(f"Company '{company_name}' not found.")
    else:
        print(f"Admin '{admin_name}' not found.")

def submit_expense(user_name, company_name, amount):
    cursor.execute("SELECT id FROM users WHERE name = %s AND role = 'user'", (user_name,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
        cursor.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
        company = cursor.fetchone()
        if company:
            company_id = company[0]
            cursor.execute("INSERT INTO expenses (company_id, user_id, amount, is_approved) VALUES (%s, %s, %s, %s)", (company_id, user_id, amount, False))
            db.commit()
            print(f"Expense of {amount} submitted for {company_name}.")
        else:
            print(f"Company '{company_name}' not found.")
    else:
        print(f"User '{user_name}' not found or not a regular user.")

def approve_expense(admin_name, company_name, expense_id):
    cursor.execute("SELECT id FROM users WHERE name = %s AND role = 'admin'", (admin_name,))
    admin = cursor.fetchone()
    if admin:
        cursor.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
        company = cursor.fetchone()
        if company:
            company_id = company[0]
            cursor.execute("UPDATE expenses SET is_approved = 1 WHERE id = %s AND company_id = %s", (expense_id, company_id))
            db.commit()
            print(f"Expense {expense_id} approved for {company_name}.")
        else:
            print(f"Company '{company_name}' not found.")
    else:
        print(f"Admin '{admin_name}' not found.")

def view_report(user_name, company_name=None):
    cursor.execute("SELECT role FROM users WHERE name = %s", (user_name,))
    role = cursor.fetchone()
    if role:
        if role[0] == 'main-admin':
            cursor.execute("SELECT companies.name, income, expenses FROM accounts JOIN companies ON accounts.company_id = companies.id")
            reports = cursor.fetchall()
            for report in reports:
                print(f"Company: {report[0]}, Income: {report[1]}, Expenses: {report[2]}")
        elif role[0] == 'owner' and company_name:
            cursor.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
            company = cursor.fetchone()
            if company:
                cursor.execute("SELECT income, expenses FROM accounts WHERE company_id = %s", (company[0],))
                account = cursor.fetchone()
                print(f"Income: {account[0]}, Expenses: {account[1]}")
            else:
                print(f"Company '{company_name}' not found.")
        else:
            print("Access denied.")
    else:
        print(f"User '{user_name}' not found.")

def main():
    while True:
        print('1. Create Company (Owner Only)')
        print('2. Add Income (Admin Only)')
        print('3. Submit Expense (User Only)')
        print('4. Approve Expense (Admin Only)')
        print('5. View Report')
        print('6. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            company_name = input('Enter the company name: ')
            owner_name = input('Enter the owner name: ')
            create_company(company_name, owner_name)
        elif choice == '2':
            admin_name = input('Enter the admin name: ')
            company_name = input('Enter the company name: ')
            amount = float(input('Enter the income amount: '))
            add_income(admin_name, company_name, amount)
        elif choice == '3':
            user_name = input('Enter the user name: ')
            company_name = input('Enter the company name: ')
            amount = float(input('Enter the expense amount: '))
            submit_expense(user_name, company_name, amount)
        elif choice == '4':
            admin_name = input('Enter the admin name: ')
            company_name = input('Enter the company name: ')
            expense_id = int(input('Enter the expense ID to approve: '))
            approve_expense(admin_name, company_name, expense_id)
        elif choice == '5':
            user_name = input('Enter the user name: ')
            company_name = input('Enter the company name (leave blank to view all): ')
            view_report(user_name, company_name)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
