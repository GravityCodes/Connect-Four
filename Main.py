# I will be making a class that handles all the features of this game.
# This game will be strickly 2 players.
# A new class object will be initialized on each new game.

class connectFour:
    
    def __init__(self, p1, p2):
        # names for p1 and p2.
        self.p1 = p1
        self.p2 = p2
        self.row = ["1", "2", "3", "4", "5", "6"]
        self.column = ["A", "B", "C", "D", "E", "F", "G"]
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
        i = 0
        
        print("\n   A    B    C    D    E    F    G")
        for x in range(self.rowNumbers):
            i += 1
            a = i - 1
            print(f' +----+----+----+----+----+----+----+')
            print(f'{i}| {gb[a][0]}  | {gb[a][1]}  | {gb[a][2]}  | {gb[a][3]}  | {gb[a][4]}  | {gb[a][5]}  | {gb[a][6]}  | ')
            
    def findspot(self, token):
       
        row = self.row
        column = self.column
           #The token should be a string of a letter and number. Ex A2
        for letter in token:
            if letter in column:
                columnIndex = column.index(letter)
        for number in token:
            if number in row:
                rowIndex = row.index(number)
                
        return columnIndex, rowIndex
    
    def p1placetk(self, token):
        gb = self.gameboard
        p1x = self.p1Token
        p2x = self.p2Token
        
        columnIndex, rowIndex = self.findspot(token)
        #Checking if the player can place the token on the desire spot.
        if gb[rowIndex][columnIndex] != 0:
            print("You can not place the token there!")
            return True
        elif rowIndex == 5:
            gb[rowIndex][columnIndex] = p1x
        elif gb[rowIndex + 1][columnIndex] == p1x or gb[rowIndex + 1][columnIndex] == p2x:
            
            gb[rowIndex][columnIndex] = p1x
        else:
            print("You can not place the token there!")
            return True
    
    def p2placetk(self, token):
        gb = self.gameboard
        p2x = self.p2Token
        p1x = self.p1Token
        columnIndex, rowIndex = self.findspot(token)
        
        #Checking if the player can place the token on the desire spot.
        if gb[rowIndex][columnIndex] != 0:
            print("There is already a token in that spot!")
            return True
        elif rowIndex == 5:
            
            gb[rowIndex][columnIndex] = p2x
            
        elif gb[rowIndex + 1][columnIndex] == p2x or gb[rowIndex + 1][columnIndex] == p1x:
            
            gb[rowIndex][columnIndex] = p2x
        
        else:
            print("You can not place the token there!")
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
            
              