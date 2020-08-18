from datetime import datetime
class Employee:
   def __init__(self, name, age, salary, employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year

   def get_working_years(self):
       return datetime.now().year - self.employment_year

   def __str__(self):
       return "name: %s age: %s salary: %s employment year %s " % (self.name, self.age, self.salary, self.employment_year)


class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        Employee.__init__(self, name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_working_years(self):
        return datetime.now().year - self.employment_year

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        return "name: %s age: %s salary: %s employment year %s bonus percentage %s " % (self.name, self.age, self.salary, self.employment_year, self.bonus_percentage)



def main():
    elist = []
    mlist = []
    while 0 == 0:
        print("----------------------\n\n----------------------\nWelcome to HR Pro 2020\n\n")
        print("Options: \n\n 1. Show Employees \n 2. Show Managers \n 3. Add An Employee \n 4. Add A Manager \n 5. Exit")
        option = input("\n\nWhat would you like to do?")
        if option == "1":
            print("Employees")
            for emp in elist:
                print(emp)
        elif option == "2":
            print("Managers")
            for mngr in mlist:
                print (mngr)
        elif option == "3":
            name = input("name: ")
            age = input("age: ")
            salary = input("salary: ")
            employment_year = input("Employement year: ")
            e = Employee(name, age, salary, employment_year)
            elist.append(e)
            print("Employee added succesfully")
        elif option == "4":
            name = input("name: ")
            age = input("age: ")
            salary = input("salary: ")
            employment_year = input("Employement year: ")
            bonus_percentage = input("bonus percentage: ")
            m = Manager(name, age, salary, employment_year, bonus_percentage)
            mlist.append(m)
            print("Manager added succesfully")
        elif option == "5":
            exit()










if __name__ == '__main__':
    main()
