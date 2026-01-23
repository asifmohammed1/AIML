#Create a Person class with the attributes name, age, and email.
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def display_details(self):
        print("Person Details:")
        print(f"  Name  : {self.name}")
        print(f"  Age   : {self.age}")
        print(f"  Email : {self.email}")
        print("-" * 30)
p1 = Person("Pravallika", 22, "pravallika@gmail.com")
p1.display_details()
p2 = Person("navya", 25, "navyadadi1999@gmail.com")
p2.display_details()


'''output:
  Person Details:
  Name  : Pravallika
  Age   : 22
  Email : pravallika@gmail.com
  ------------------------------
  Person Details:
  Name  : navya
  Age   : 25
  Email : navyadadi1999@gmail.com
  ------------------------------
