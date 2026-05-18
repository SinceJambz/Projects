"""
Author: José Bejarano
Course: CSEPC110
Teacher: Thomas Koster
Assigment: Clever Stories

"""
Name = input("Hi user! What is your name? ")
# blank line
print()
print(
    F"Perfect! Nice to meet you {Name} so let me tell you a story created by yourself just put in the chat verbs, exclamations adjecive and animal to use and the story")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Variables to use at the story
print(F"{Name}, please enter the following")

adjective = input("adjective ")
animal = input("animal ") 
verb1 = input("verb ")
exclamation = input("exclamation ")
verb2 = input("other verb ")
verb3 = input("one more verb ")

print()

print("The story is starting....")

print()
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Story being using in

print(
    f"The other day, I was really in trouble. "
    f"It all started when I saw a very {adjective} {animal} "
    f"{verb1} down the hallway. "
    f'"{exclamation.capitalize()}!" I yelled. '
    f"But all I could think to do was {verb2} over and over. "
    f"Miraculously, that caused it to stop, "
    f"but not before it tried to {verb3} right in front of my family."
)
print()
print("Thanks for all!")
