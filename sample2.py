title = input("enter the title of the book: ")
author = input("enter the  author of the book: ")
price = input("enter the price of the book: ")
quantity =input("enter the quantity: ")
purchase = input("Enter  the purchase quantity: ")

print("Book Details:")
print("Title: "+title)
print("Author: "+author)
print("Price: "+price)
print("Stock: "+quantity)

if(purchase>=quantity):
    print("The Book "+title+ " is in stock")
else:
    print("The Book is out of stock")
