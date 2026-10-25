#This is one of my first python scripts. It asks for the right pin.
#If the wrong pin is entered, it will ask only specific times before it locks you out.

#Creating the correct pin
pin = "6767"


#Resetting the number of attempts
attempts = 0

#Setting the maximum attempts to a specific value
max_attempts = 5

#Printing the welcome message 

print(" === Security Login Check === ")

#Starting the while loop to check for the pin 3 times
while attempts < max_attempts:

    text = input("Please enter your pin: ")

#adding 1 to the attempts variable each time the loop runs
    attempts += 1  

#If statement
    if text == pin:
        print("Access granted")
        break

#Else clause
    else: 
    #If attempts reached 3, the programm stops
        if attempts == max_attempts:
            print("You have been locked out! Please contact the administrator!")

        else:
            print("Wrong pin! Please try again!")
            print("Attempts remaining:" ,max_attempts - attempts,)    
