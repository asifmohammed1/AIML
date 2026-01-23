#Write a Book class that has a title, author, and price attributes. Implement a method to apply a discount to the book's price.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            print("Invalid discount percentage!")
            return
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        print(f"Discount of {percentage}% applied!")
        print(f"New price: ₹{self.price:.2f}")
    def display_info(self):
        print("Book Details:")
        print(f"  Title  : {self.title}")
        print(f"  Author : {self.author}")
        print(f"  Price  : ₹{self.price:.2f}")
        print("-" * 30)


'''output:
Book Details:
  Title  : Python for Beginners
  Author : John Smith
  Price  : ₹599.00
------------------------------
Discount of 15% applied!
New price: ₹509.15
Book Details:
  Title  : Python for Beginners
  Author : John Smith
  Price  : ₹509.15
------------------------------'''
