# I will be making a class that handles all the features of this game.
# This game will be strickly 2 players.
# A new class object will be initialized on each new game.

class connectFour:
    
    def __init__(self, p1, p2):
        # names for p1 and p2.
        self.p1 = p1
        self.p2 = p2
        self.row = ["1", "2", "3", "4", "5", "6"]
        self.column = ["1", "2", "3", "4", "5", "6", "7"]
        self.gameboard = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.columnNumbers = 7
        self.rowNumbers = 6
        self.p1Token = "\u001b[0;31mX\u001b[0m"
        self.p2Token = "\u001b[;33mO\u001b[0m"
        
    # Prints the gameboard to the terminal    
    def printgb(self):
        gb = self.gameboard
        
        print("\n   1    2    3    4    5    6    7")
        for a in range(self.rowNumbers):
            print(f' +----+----+----+----+----+----+----+')
            print(f' | {gb[a][0]}  | {gb[a][1]}  | {gb[a][2]}  | {gb[a][3]}  | {gb[a][4]}  | {gb[a][5]}  | {gb[a][6]}  | ')
            
    def p1placetk(self, token):
        gb = self.gameboard
        p1x = self.p1Token
        column = self.column
        #The token should be a number from 1 to 7. Ex A2
        if token in column:
            columnIndex = column.index(token)
            #Checking if the player can place the token on the desire spot.
            for row in reversed(range(6)):
                if gb[row][columnIndex] == 0:
                    gb[row][columnIndex] = p1x
                    break
            else:
                print("That column is full")
                return True
        else:
            print("That is not a valid play")
            return True

    def p2placetk(self, token):
        gb = self.gameboard
        p2x = self.p2Token
        column = self.column
           #The token should be a number from 1 to 7. Ex A2
    
       
        if token in column:
            columnIndex = column.index(token)
            #Checking if the player can place the token on the desire spot.
            for row in reversed(range(6)):
                if gb[row][columnIndex] == 0:
                    gb[row][columnIndex] = p2x
                    break
            else:
                print("That column is full")
                return True
        else:
            print("That is not a valid play")
            return True
            
    def checkwinner(self, piece):
        gb = self.gameboard
        
        #Check horizontal locations
        for c in range(self.columnNumbers - 3):
            for r in range(self.rowNumbers):
                if gb[r][c] == piece and gb[r][c +1] == piece and gb[r][c+2] == piece and gb[r][c+3] == piece:
                    print("You won!")
                    return True
        #Check Vertical Locations
        for r in range(self.rowNumbers - 3):
            for c in range(self.columnNumbers):
                if gb[r][c] == piece and gb[r + 1][c] == piece and gb[r + 2][c] == piece and gb[r + 3][c] == piece:
                    print("You won!")
                    return True
        #Check for left to right diagonal locations
        for c in range(self.columnNumbers -3):
            for r in range(self.rowNumbers-1, 3, -1): 
              if gb[r][c] == piece and gb[r-1][c+1] == piece and gb[r-2][c+2] == piece and gb[r-3][c+3] == piece:
                  print("You won!")
                  return True
        #Check for right to left diagonal locations
        for c in range(self.columnNumbers-1,4,-1):
            for r in range(self.rowNumbers-1, 3, -1): 
              if gb[r][c] == piece and gb[r-1][c-1] == piece and gb[r-2][c-2] == piece and gb[r-3][c-3] == piece:
                  print("You won!")
                  return True
              