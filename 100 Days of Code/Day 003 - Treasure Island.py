print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You leave the boat and walk down across the beach until you reach a fork in the path")
print('''
    _\/_                        _\/_
    /o\\\                        //o\\
     |                           |
    _|___________________________|__''')
left_or_right = input("You can either walk into the forest on the right or follow the beach to the left, which do you do? (Left or right):\n")

if left_or_right.lower() != "left":
  print("You fall into a hole.\nGame Over.")
  exit()

print("You keep walking down the beach until you see a body of water seperating you from the continuing any further.")
print('''
    _\/_                 |                _\/_
    /o\\\             \       /            //o\\
     |                 .---.                |
    _|_______     --  /     \  --     ______|__
             `~^~^~^~^~^~^~^~^~^~^~^~`''')
swim_or_wait = input("You can either swim across to the other side or wait where you are, which do you do? (Swim or wait):\n")

if swim_or_wait.lower() != "wait":
  print("Attacked by trout.\nGame Over.")
  exit()

print("While waiting and looking out across the water you see a large tree drifting down the water that almost reaches across the entire gap.\nYou jump onto the tree, quickly run across while balancing and just make it to the other side./nYou keep walking down the beach until you come across a house in the trees on your left. It is a strange looking house with 3 different coloured doors. ")
print('''
    _m_   
  /\___\    
  |_|""|    
_/______\___
''')

red_yellow_blue = input("Which door do you open? (Red, yellow or blue):\n")

if red_yellow_blue.lower() == "red":
  print("Burned by fire.\nGame Over.")
  exit()

elif red_yellow_blue.lower() == "blue":
  print("Eaten by beasts.\nGame Over.")
  exit()
  
elif red_yellow_blue.lower() == "yellow":
  print("You Win!")
  exit()
else:
  print("Game Over.")
  exit()
