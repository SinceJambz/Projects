"""
Author: José Bejarano

Purpose: Meal Price Calculator

"""

# Restaurant Name
restaurant_name = "Bejarano Family Restaurant"

# Greeting
machine_name = "José"


print(f"Welcome to {restaurant_name}")
print()

user_name = input(f"My name is {machine_name}! What is your name? ")

print()

print(f"Nice to meet you {user_name}!")

print()


# Data

child_meal = float(input("What is the price of a child's meal? "))
print()

adult_meal = float(input("What is the price of an adult's meal? "))
print()

children_amount = int(input("How many children are there? "))
print()


adult_amount = int(input("How many adults are there? "))
print()

# Calculation
subtotal_calculate = (child_meal * children_amount) + \
    (adult_meal * adult_amount)


print(f"Subtotal: ${subtotal_calculate:.2f}")


# Sales Tax
sales_tax = float(input("What is the sales tax rate?"))

# Total
total = subtotal_calculate + sales_tax
print()
print(f"Total: ${total:.2f}")
print()

# Payment Amount
payment_amount = float(input("What is the payment amount? "))

# change
change = payment_amount - total

print(f"Change: ${change:.2f}")

print("thanks for using Meal Price Calculator")

# Receipt
print("------ Receipt ------")
print(f"Children Meals: {children_amount}")
print(f"Adult Meals:    {adult_amount}")
print(f"Subtotal:       ${subtotal_calculate:.2f}")
print(f"Sales Tax:      ${sales_tax:.2f}")
print(f"Total:          ${total:.2f}")
print(f"Payment:        ${payment_amount:.2f}")
print(f"Change:         ${change:.2f}")
print("----------------------")

# i tried to do a receipt

print()

print("Thanks for using Meal Price Calculator!")
