class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")

    def get_salary(self):
        return self.__salary

    def display(self):
        print("\nEmployee Name :", self.name)
        print("Salary        : $", self.__salary)


# Main Program

name = input("Employee Name: ")
salary = float(input("Salary: "))

emp = Employee(name, salary)

emp.display()

new_salary = float(input("\nEnter New Salary: "))
emp.set_salary(new_salary)

print("\nUpdated Information")
emp.display()
