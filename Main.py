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
        
        print("\n   A  B  C  D  E  F  G")
        for x in gb:
            i += 1
            print(f'{i} {x} \n')
            
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

        gb[columnIndex][rowIndex] = 'X'
    
    def p2placetk(self, token):
        gb = self.gameboard
       
        columnIndex, rowIndex = self.findtoken(token)
       
        gb[columnIndex][rowIndex] = 'O'