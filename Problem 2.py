#Deshawn Smith
#04/09/2019

#Problem 2 this will tell you the number of day of the week you returned on.

day = int(input("number 0 - 6")) # Confusing on a user part. Might say "enter"

gone = int(input("How long were you gone?")) 

gone % 7 # What is this line doint?

((gone % 7) + day) # What is this line doing?
print(((gone % 7) + day) % 7)
