# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State. 
# Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.

import json
class Employee:
  def __init__(self):
    pass
  def create_file(self):
    self.employee_info={1:{"Name":"Suman","DOB":"01/01/1997","Height":"5'6","City":"Pune","State":"Maharastra"},
                        2:{"Name":"Sree","DOB":"13/10/1999","Height":"5'2","City":"Guntur","State":"Andhra Pradesh"},
                        3:{"Name":"Lakshmi","DOB":"28/03/1998","Height":"5'0","City":"Hyderabad","State":"Telengana"},
                        4:{"Name":"Shiny","DOB":"31/05/1998","Height":"4'9","City":"Banglore","State":"Karnataka"},
                        5:{"Name":"Anirudh","DOB":"16/10/1994","Height":"6'0","City":"Chennai","State":"Tamil Nadu"}}
    with open("employee.json","w") as f:
      d=json.dump(self.employee_info,f)
      print('json file is created')
    print('-'*25)
  def reads_info(self):
    with open("employee.json","r") as f:
      x=json.load(f)
      print("List of the Employee objects are :")
      for i in x.values():
        l=[]
        l.append(i)
        print(l)
      print(type(l))

obj=Employee()
obj.create_file()
obj.reads_info()

# Output

# json file is created
# -------------------------
# List of the Employee objects are :
# [{'Name': 'Suman', 'DOB': '01/01/1997', 'Height': "5'6", 'City': 'Pune', 'State': 'Maharastra'}]
# [{'Name': 'Sree', 'DOB': '13/10/1999', 'Height': "5'2", 'City': 'Guntur', 'State': 'Andhra Pradesh'}]
# [{'Name': 'Lakshmi', 'DOB': '28/03/1998', 'Height': "5'0", 'City': 'Hyderabad', 'State': 'Telengana'}]
# [{'Name': 'Shiny', 'DOB': '31/05/1998', 'Height': "4'9", 'City': 'Banglore', 'State': 'Karnataka'}]
# [{'Name': 'Anirudh', 'DOB': '16/10/1994', 'Height': "6'0", 'City': 'Chennai', 'State': 'Tamil Nadu'}]
# <class 'list'>
