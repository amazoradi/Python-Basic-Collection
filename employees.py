# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
class Employee:
  def __init__(self, name, gender,  title, start_date):
    # self.company_name = company
    self.employee_name = name
    self.gender = gender
    self.job_title = title
    self.start_date = start_date

  def pronoun_getter(self):
    if self.gender == "female":
      return "She is"
    elif self.gender == "male":
      return "He is"
    else:
      return "They are"

  # def __str__(self):
  #   return f"The employee's name is {self.employee_name}. {self.pronoun_getter()} the {self.job_title} and started working at {self.company_name} on {self.start_date}."

# print(Sadie)





class Company(object):
    """This represents a company in which people work"""
    def __init__(self, company_name, date_founded):
      self.company_name = company_name
      self.date_founded = date_founded
      self.employees  = []
        

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    def add_employee(self, employee):
      return self.employees.append(employee)

    def hire_employee(self, title, date):
      self.title = title
      self.start_date = date
    
    def print_employees(self):
      
      for employee in self.employees:
       print(f"The employee, {employee.employee_name}, is the {employee.job_title} and started working at {self.company_name} (which was founded on {self.date_founded}) on {employee.start_date}.")
      

Sadie = Employee("Sadie Zoradi", "female", "Director of YM", "Aug 2015")
Marshall = Employee("Marshall Clark", "male", "Assistant", "May 2018")
Lee = Employee("Lee Spruill", "male", "Boss Man", "June 2010")
st_g = Company("St Gs", "1902")
st_g.add_employee(Sadie)
st_g.add_employee(Marshall)
st_g.add_employee(Lee)



st_g.print_employees()


# # Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
# class Employee:
#   def __init__(self,  title, start_date):
#     # self.company_name = company
  
#     self.job_title = title
#     self.start_date = start_date

#   def pronoun_getter(self):
#     if self.gender == "female":
#       return "She is"
#     elif self.gender == "male":
#       return "He is"
#     else:
#       return "They are"

#   # def __str__(self):
#   #   return f"The employee's name is {self.employee_name}. {self.pronoun_getter()} the {self.job_title} and started working at {self.company_name} on {self.start_date}."

# # print(Sadie)

# class Worker:
#   def __init__(self, name, gender):
#     # self.company_name = company
#     self.employee_name = name
#     self.gender = gender

#   def pronoun_getter(self):
#     if self.gender == "female":
#       return "she"
#     elif self.gender == "male":
#       return "he"
#     else:
#       return "they"


# class Company(object):
#     """This represents a company in which people work"""
#     def __init__(self, company_name, date_founded):
#       self.company_name = company_name
#       self.date_founded = date_founded
#       self.employees  = []
        

#     def get_company_name(self):
#         """Returns the name of the company"""

#         return self.company_name

#     def add_employee(self, worker, title, date):
#       employee = Employee(worker, title, date)
#       return self.employees.append(employee)
      

    
    
#     def print_employees(self):
#       for employee in self.employees:
#        print(f"The employee, {employee.employee_name}, is the {employee.job_title} and started working at {self.company_name} (which was founded on {self.date_founded}) on {employee.start_date}.")

   
      

# # Sadie = Employee("Sadie Zoradi", "female", "Director of YM", "Aug 2015")
# # Marshall = Employee("Marshall Clark", "male", "Assistant", "May 2018")
# # Lee = Employee("Lee Spruill", "male", "Boss Man", "June 2010")
# # st_g = Company("St Gs", "1902")
# # st_g.add_employee(Sadie)
# # st_g.add_employee(Marshall)
# # st_g.add_employee(Lee)



# # st_g.print_employees()


# Sadie = Worker("Sadie Zoradi", "female")
# st_g = Company("St Gs", "1902")
# st_g.add_employee(Sadie, "Director of YM", "Aug 2015" )
# st_g.print_employee()




# try: 

# except KeyError


