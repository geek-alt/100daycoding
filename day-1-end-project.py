#End of the day project: Band name generator
import time
'''
Ask user for city that they grew up in (The cursor show start in new line)

Ask user for what is their pet name

After combine or concatenate the user input to give Band name for the user

'''
# in this code i wanted to check if the user has entered pet name or left it blank. I wanted to use if and else statement. but couldn't find how to. my vision was 
'''
-----
---
if pet_name:
    ""
else:
    print("Please enter a valid pet name:/n") that is backslash.



'''
print("Connecting..")
time.sleep(0.9)
print("....")
print("Installing Packages ...")
print("Starting Program ....\n***Welcome to Band Name Generator***")
time.sleep(0.9)

def get_pet_name():
    pet_name = input("What is the name of your pet?\n")

    if pet_name.strip():
        return pet_name
    else:
        print("Please enter the pet name")
        return get_pet_name()

city = input("What is your city name?\n")

print("Generating Band Name \nPlease wait.....")
time.sleep(3)

band_name = print("The name for your band is " + city + " " + get_pet_name())