"""
Author: José Bejarano 

Purpose: Areas of Shapes
"""
#importing math library 
import math

#We've two variables to the machine and user interaction
Machine_Name = "José"
User_Name = input(f"Hi! My name is {Machine_Name}! What is your name? ")

#blank line
print()

print(f"Nice to meet you {User_Name}! I'm so excited and We gonna start with Areas of Shape let's do it! ")


#three shape's options 
Option = input(f"""
  Perfect {User_Name} ! Choose one of these three option below.
  Square
  rectangle
  Circle """).lower()

#Doing a count
if Option == "square":
  
  #area of a square
  side = float(input("What is the length of a side of the square? "))
  area = side ** 2
  print(f"The area of the square is: {area} ")

 

elif Option == "rectangle"  :
  length = float(input("What is the length of rectangle? "))
  width = float(input("What is the width of the rectangle? "))
  area = length * width
  print(f"The area of the rectangle is: {area} ")



elif Option ==  "circle" :

    radius = float(input("What is the radius of the circle? "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area} ")



else:
  print (f" I can't do it ")



#three shape's options 
Option = input(f"""
  Perfect {User_Name} ! Choose one of these three option below.
  Square
  rectangle
  Circle """).lower()

#Doing a count
if Option == "square":
  
  #area of a square
  side = float(input("What is the length of a side of the square? "))
  area = side ** 2
  print(f"The area of the square is: {area} ")

 

elif Option == "rectangle"  :
  length = float(input("What is the length of rectangle? "))
  width = float(input("What is the width of the rectangle? "))
  area = length * width
  print(f"The area of the rectangle is: {area} ")



elif Option ==  "circle" :

    radius = float(input("What is the radius of the circle? "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area} ")



else:
  print (f" I can't do it ")

  #three shape's options 
Option = input(f"""
  Perfect {User_Name} ! Choose one of these three option below.
  Square
  rectangle
  Circle """).lower()

#Doing a count
if Option == "square":
  
  #area of a square
  side = float(input("What is the length of a side of the square? "))
  area = side ** 2
  print(f"The area of the square is: {area} ")

 

elif Option == "rectangle"  :
  length = float(input("What is the length of rectangle? "))
  width = float(input("What is the width of the rectangle? "))
  area = length * width
  print(f"The area of the rectangle is: {area} ")



elif Option ==  "circle" :

    radius = float(input("What is the radius of the circle? "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area} ")



else:
  print (f" I can't do it ")



print()

print(f"Thanks for using the calculator")