class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name == target_name]
        return result

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == "<":
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            result = []
        return result

def main():
    table = EmployeeTable()

    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    table.add_employee(emp1)
    table.add_employee(emp2)
    table.add_employee(emp3)
    table.add_employee(emp4)
    table.add_employee(emp5)

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (> < <= >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        target_age = int(input("Enter the age to search: "))
        result = table.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search: ")
        result = table.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter the operator (> < <= >=): ")
        target_salary = int(input("Enter the salary to search: "))
        result = table.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("Search Result:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found")

if __name__ == "__main__":
    main()
