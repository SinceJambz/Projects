"""
Author: José Bejarano

Purpose: Practice formatting strings with an ID Badge program.

"""

print("Please enter the following information: ")
# this prints a blank line
print()
First_Name = input("First name: ").upper() 
Last_Name = input("Last name: ").upper() 
Email = input("email: ").lower()
Phone = input("phone number: ") 
Job_Title = input("Job tittle: ").upper() 
ID_Number = input("ID Number: ").upper() 
# this prints a blank line
print()
#This time I used a/n make a blank line before this: 
print("The ID Card is: ")
print("-----------------------------------------------")
print(f"{Last_Name}, {First_Name} ")
print(Job_Title)
print(ID_Number)
# blank line
print()
print(Email)
print(Phone)
print("-----------------------------------------------")
