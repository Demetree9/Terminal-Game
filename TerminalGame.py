import random

#Dice Roller:
def roll_d_4(number):   
    d_4 = 0
    for i in range(number):
      d_4 = d_4 + random.randint(1,4)
    return d_4 

def roll_d_6(number):   
    d_6 = 0
    for i in range(number):
      d_6 = d_6 + random.randint(1,6)
    return d_6    

def roll_d_8(number):
   d_8 = 0
   for i in range(number):
    d_8 = d_8 + random.randint(1,8)
   return d_8

def roll_d_10(number):
   d_10 = 0
   for i in range(number):
      d_10 = d_10 + random.randint(1,10)
   return d_10

def roll_d_12(number):
   d_12 = 0
   for i in range(number):
      d_12 = d_12 + random.randint(1,12)
   return d_12
   
def roll_d_20(number):
   d_20 = 0
   for i in range(number):
      d_20 = d_20 + random.randint(1,20)
   return d_20

#: user input initialization:


#Invalid input for Y/N function:
# def error_catcher():
#    while user_input_1.upper() != "Y" and "N":
#       print('Invalid entry! Type "Y" or "N" to continue')
#       user_input_1 = input()
#       if user_input_1.upper() == "Y" or "N":
#          break

#Menu:
print("Hello there! Are you ready for an adventure!? (Y/N) ")
user_input_1 = input()

#Start of Story:
while (user_input_1.upper() != "Y" or "N"):
   print('Invalid entry! Type "Y" or "N" to continue')
   user_input_1 = input()
   if user_input_1.upper() == "Y" or "N":
      break

while user_input_1.upper() == "N":
      print("Okay...I guess I'll just wait until you are...")
      print("Hello there! Are you ready for an adventure now!? (Y/N) ")
      user_input_1 = input()
      if user_input_1.upper() == "Y": 
         break
      

if user_input_1.upper() == "Y":
    print("Good! Then we're off on an adventure!")
    print("You enbark from the city of Varrock, heading south to Lumbridge.")
    print("You have your horse all loaded up with valubles to trade to the townsfolk when you arive.")      

#First Event Determined by a D4:
random_event_1 = roll_d_4(1)

#If a 1 is rolled:
if random_event_1 == 1:
   print("As you are traveling the long road to the south, two individuals stop you.")
   print('"Hey you!" They scream. "Give us all your stuff or else!"')
   print("What do you do? (1,2,3)")
   print("1. Give them all your stuff")
   print("2. Fight them!")
   print("3. Run past them!")

   user_input_2 = input()

   #Invalid input:
   while int(user_input_2) == int(1) and int(2) and int(3):
         print("Invalid response.")
         user_input_2 = input()
         if user_input_2 == 1 or 2 or 3:
            break

#If option 1, player hands their stuff over:
   if int(user_input_2) == int(1):
      print("You hand over all your stuff, and the individuals move on their way.")


    #If option 2, they fight or die.
   elif int(user_input_2) == int(2):
      print('"Prepare to meet your doom!"')
      print("You must roll at least a 10 on a D20 to defeat these scum! (type: roll)")
      user_input_3 = input()
      while user_input_3.lower() != "roll":
         print('Invalid command. Try typing "roll"')
         user_input_3 = input()
         if user_input_3.lower() == "roll":
            break
      if user_input_3 == "roll":
         first_d_20 = roll_d_20(1)
         print(first_d_20)
         if first_d_20 >= 10:
            print("You easily defeat the two punks and go about your day.")
         else: 
            print("You are defeated!") #Need to send back to beginning.


    #Option 3 the player tries to run.
   elif int(user_input_2) == int(3):
      print("You snap your reins and take off.")
      print("You will need to roll above a 9 to get away. Are you ready? (Y/N)")
      user_input_4 = input()
      while user_input_4.upper() != "Y":
         print("Alright...type Y when you're ready.")
         user_input_4 = input()
      if user_input_4.upper() == "Y":
            d_20_roll = roll_d_20(1)
            print(d_20_roll)
            if d_20_roll >= 9:
               print("Your horse is too fast and you get away.")
            else:
               print("They manage to catch you as you run and defeat you.") #Send back to beginning.
   
#Second Event if 2 is rolled on the D4:
if random_event_1 == 2:
   print("As you are traveling, you see an individual in a rainbow suit approach you.")
   print('"Hey you!" He exclaims, "Do you want to hear some jokes? (Y/N)')
   user_input_1 = input()

#Error Catcher:
   while user_input_1.upper() == "Y" and "N":
      print('Invalid entry. Try "Y" or "N"')
      user_input_1 = input()
      if user_input_1 == "Y" or "N":
         break

#Bard interaction:
   if user_input_1.upper() == "N":
      print('"No thanks," you say as you continue on your way.')
   elif user_input_1.upper() == "Y":
      print("Sure you say. Let's hear them.")
      print('"Okay," says the individual, "What is the difference between a hippo and a zippo?"')
      print('Type "?" when you are ready')

#First Joke:
   #Error Catcher:
      user_input_2 = input()
      while user_input_2 != "?":
         print('Did you type "?"')
         user_input_2 = input()
         if user_input_2 == "?":
            break
   #Punchline:      
      if user_input_2 == "?":
         print("Well one's heavy and one's a little lighter.")

#Second Joke Option:
         print("Do you want to hear another? (Y/N)")
         user_input_3 = input()

   #Error Catcher:       
         while user_input_3.upper() != "Y" and "N":
            print('Invalid entry. Try "Y" or "N"')
            user_input_3 = input()
            if user_input_3.upper() == "Y" or "N":
               break
   #Joke 2:
         if user_input_3.upper() == "Y":
            print("Okay. What do you call a person with a nose, but no body?")
            print('Type "?" when you are ready')
            user_input_4 = input()

   #Error Catcher:         
            while user_input_4 != "?":
               print('Did you type "?"')
               user_input_4 = input()
               if user_input_4 == "?":
                  break

   #Punchline:            
            if user_input_4 == "?":
               print("Nobody knows!")
               print("Well that's all I have time for. Have a nice day, and thanks for listening!")

#Third event if a 3 is rolled:
if random_event_1 == 3:
   print("As you are traveling along the road, a storm begins to brew. What should you do?")
   print("1. Take shelter immediately!")
   print("2. Keep going, you'll be fine.")
   print("Input 1 or 2.")
   user_input_1 = input()

   #Error Catcher:
   while user_input_1 != int(1) and int(2):
      print('Invalid input. Try "1" or "2"')
      user_input_1 = input()
      if user_input_1 == int(1) or int(2):
         break

   #Choices:
   if int(user_input_1) == 1:
      print("You take shelter from the storm and it eventually passes. A good choice.")

   elif int(user_input_1) == 2:
      print("You decide to keep going, but storm continues.")
      print("You'll have to be lucky to get out of this one unharmed.")
      print("If you can roll a 15 or higher, you can weather the storm and make it to your destination. Are you ready? (Y/N)")
      user_input_2 = input()

      #Error Catcher: THIS ONE WORKS FOR SOME REASON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      while user_input_2.upper() != "Y" and "N":
            print('Invalid entry. Try "Y" or "N"')
            user_input_2 = input()
            if user_input_2.upper() == "Y" or "N":
               break
      #If not ready:
      if user_input_2.upper() == "N":
         print("Okay...hopefully something bad doesn't happen as you wait...")
         print("Are you ready now? (Y/N)")
         user_input_2 = input()
         if user_input_2.upper() == "N":
            print("As you hesitate, a bolt of lighting strikes you down...what bad luck.")
         elif user_input_2 == "Y":
            d_20_roll = roll_d_20(1)
            if d_20_roll >= 15:
               print("You make it to Lumbridge as the sun finally comes out.")
            else:
               print("The strong winds, rain and thunder are too much for you and your horse to bear.")
               print("You are hopelessly lost.") #Send back to beginning. 

      #If ready:
      if user_input_2.upper() == "Y":
         d_20_roll = roll_d_20(1)
         if d_20_roll >= 15:
            print("You make it to Lumbridge as the sun finally comes out.")
         else:
            print("The strong winds, rain and thunder are too much for you and your horse to bear.")
            print("You are hopelessly lost.") #Send back to beginning. 

#Last event if 4 is rolled:
if random_event_1 == 4:
   print("You have a very pleasant journey to Lumbridge and get there just as the shops open.")

print("Congradulations, you made it to Lumbridge.")