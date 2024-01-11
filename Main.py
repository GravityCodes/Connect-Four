# I will be making a class that handles all the features of this game.
# This game will be strickly 2 players.
# A new class object will be initialized on each new game.

class connectFour:
    
    def __init__(self, p1, p2):
        # names for p1 and p2.
        self.p1 = p1
        self.p2 = p2
        self.row = ["A", "B", "C", "D", "E", "F", "G"]
        self.column = ["1", "2", "3", "4", "5", "6"]
        self.gameboard = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        
    # Prints the gameboard to the terminal    
    def printgb(self):
        gb = self.gameboard
        i = 0
        
        print("\n   A    B    C    D    E    F    G")
        for x in range(6):
            i += 1
            a = i - 1
            print(f' +----+----+----+----+----+----+----+')
            print(f'{i}| {gb[a][0]}  | {gb[a][1]}  | {gb[a][2]}  | {gb[a][3]}  | {gb[a][4]}  | {gb[a][5]}  | {gb[a][6]}  | ')
            
    def findtoken(self, token):
       
        row = self.row
        column = self.column
           #The token should be a string of a letter and number. Ex A2
        for letter in token:
            if letter in row:
                rowIndex = row.index(letter)
        for number in token:
            if number in column:
                columnIndex = column.index(number)
                
        return columnIndex, rowIndex
    
    def p1placetk(self, token):
        gb = self.gameboard
        
        columnIndex, rowIndex = self.findtoken(token)
        #Checking if the player can place the token on the desire spot.
        if columnIndex == 5:
            
            gb[columnIndex][rowIndex] = 'X'

        elif gb[columnIndex + 1][rowIndex] == 'X' or gb[columnIndex + 1][rowIndex] == 'O':
            
            gb[columnIndex][rowIndex] = 'X'
        
        else:
            print("You can not place the token there!")
            return True
    
    def p2placetk(self, token):
        gb = self.gameboard
       
        columnIndex, rowIndex = self.findtoken(token)
        
        #Checking if the player can place the token on the desire spot.
        if columnIndex == 5:
            
            gb[columnIndex][rowIndex] = 'O'
            
        elif gb[columnIndex + 1][rowIndex] == 'X' or gb[columnIndex + 1][rowIndex] == 'O':
            
            gb[columnIndex][rowIndex] = 'O'
        
        else:
            print("You can not place the token there!")
            return True