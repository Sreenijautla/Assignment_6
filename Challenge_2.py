# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:
# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

class Dog:
  def __init__(self,name,age,coat_color):
    self.name=name
    self.age=age
    self.coat_color=coat_color
  def description(self):
    print('Name of the dog is',self.name)
    print('Age of the dog is',self.age,'years')
  def get_info(self):
    print('Coat color is',self.coat_color)
class JackRussellTerrier(Dog):
  def food(self):
    print('Food for this dog breed is Pedigree')
  def family(self):
    print("It's a perfect family dog")
class Bulldog(Dog):
  def country(self):
    print('It is a british breed dog')
  def cost(self):
    print("Cost price of this dog breed varies from 10,000 Rs to 60,000 Rs in India")

a=JackRussellTerrier('Ellie',7,'Purple')
a.description()
a.get_info()
a.food()
a.family()
print('-'*30)
b=Bulldog('Buddy',2,'Orange')
b.description()
b.get_info()
b.country()
b.cost()

# Output

# Name of the dog is Ellie
# Age of the dog is 7 years
# Coat color is Purple     
# Food for this dog breed is Pedigree
# It's a perfect family dog
# ------------------------------
# Name of the dog is Buddy
# Age of the dog is 2 years
# Coat color is Orange
# It is a british breed dog
# Cost price of this dog breed varies from 10,000 Rs to 60,000 Rs in India