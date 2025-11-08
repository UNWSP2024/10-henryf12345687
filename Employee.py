#Henry Forst
#Week 10
#11/07/2025
# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    def get_name(self):
        return self.name
    def get_id_number(self):
        return self.id_number
    def get_department(self):
        return self.department
    def get_job_title(self):
        return self.job_title
def main():
    employee1 = Employee("Susan Meyers"	, 47899 , "Accounting",	"Vice President")
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    print("Name       Id Number    Department    Job Title")
    print(f"{employee1.get_name()} | {employee1.get_id_number()} | {employee1.get_department()} | {employee1.get_job_title()}")
    print(f"{employee2.get_name()} | {employee2.get_id_number()} | {employee2.get_department()} | {employee2.get_job_title()}")
    print(f"{employee3.get_name()} | {employee3.get_id_number()} | {employee3.get_department()} | {employee3.get_job_title()}")
if __name__ == "__main__":
    main()