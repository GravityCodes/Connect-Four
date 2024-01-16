from Main import connectFour

# User inputs and gameplay will be programmed in this file.

print("Welcome to Connect four! \n")
print("Each player will take turns to place a token. To place a toke type the according coordinates. \
Ex.\"A2\" \n")

p1 = input("What is player's 1 name? \n")
p2 = input("What is player's 2 name? \n")
Turns = 0
Game1 = connectFour(p1, p2)

print("The Game has started! \n")

while True:
    Game1.printgb()
    p1Turn = True
    p2Turn = True
    Turns += 1
    
    while p1Turn == True:
        p1move = input(f" player 1 {p1}, Where would you like to place your token? ex. B4 \n").upper()

        p1Turn = Game1.p1placetk(p1move)
        
    if Game1.checkwinner(Game1.p1Token) == True:
         Game1.printgb()
         break
    
    
    Game1.printgb()
    Turns += 1
    while p2Turn == True:
        p2Move = input(f" player 2 {p2}, Where would you like to place your token? ex. A3 \n").upper()
   
        p2Turn = Game1.p2placetk(p2Move)
    
    if Game1.checkwinner(Game1.p2Token) == True:
        Game1.printgb()
        break
        
    if Turns == 42:
        print("Tied!")
        break
