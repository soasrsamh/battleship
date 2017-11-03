##################################################################################################################
##################################################################################################################
###### Battleship
###### S.L. Howell November 2017
###### Earnest Coding Challenge 
######
###### In this simplified version of battleship, a board is simply a grid of potentially attacked positions along
###### with one or more ships each of which occupy one or more positions. This script models a board
###### and implements the attack function for a board and position. Managing multiple players, reading
###### user input, or actually playing a game is beyond the scope of the exercise, which is focused
###### only on the state and logic required to execute a single attack.
###### 
###### An attack results in the new state of the board along with one of the following outcomes:
######  'Hit' if there is a ship occupying the position
######  'Miss' if no ships occupy the position
######  'Already Taken' if the position has previously been attacked
######  'Sunk' if the attack hits the last remaining position of a ship
######  'Win' if the attack sinks the last remaining ship
##################################################################################################################
##################################################################################################################

from random import *


##################################################################################################################
#### class Board
##################################################################################################################

# A board is simply a grid of potentially attacked positions along 
# with one or more ships each of which occupy one or more positions.
# which is composed of ships which can be attacked.
class Board:

    # Initializes and returns a new Board object.
    # boardWidth is the length (int) of the side of the board. (must be at least one)
    # boardHeight is the height (int) of the side of the board. (must be at least one)
    # ships is a list of Ship objects that are on the board. (must be at least one)
    def __init__(self, boardWidth, boardHeight, ships):
        
        #Test that the input is of the expected type and expected size.
        if type(boardWidth) is not int or type(boardHeight) is not int or type(ships) is not list:
            raise Exception("This board could not be created because one or more inputs were of an unexpected type.")
        if boardWidth < 1 or boardHeight < 1 or len(ships) < 1:
            raise Exception("This board was not created because a board must have at least one potentially attacked \
                    position along with one or more ships.")
        
        self.boardWidth = boardWidth      # boardWidth is the length of the side of the board.
        self.boardHeight = boardHeight    # boardHeight is the height of the side of the board.
        self.ships = ships                # ships is a list of Ship objects that are on the board.
        
        # Denote the condition (water, hit, or miss) of a position with a character
        self.water = 'W'
        self.hit = 'X'
        self.miss = 'M'
        
        # Initialize an empty board (with only water)
        self.grid = [[self.water for j in range(self.boardHeight)] for i in range(self.boardWidth)]
        
        
        # Keep track of how many ships are on the board and have been sunk
        self.numShips = 0
        self.numSunk = 0 
        
        # Denote the existence of a ship at a position with the ship's id
        for id in range(len(self.ships)):
            self.placeShip(self.ships[id],id)


    # An attack takes in the x, y coordinates of an attack (both ints).
    # An attack results in the new state of the board along with one of the following outcomes:
    # 'Hit' if there is a ship occupying the position
    # 'Miss' if no ships occupy the position
    # 'Already Taken' if the position has previously been attacked
    # 'Sunk' if the attack hits the last remaining position of a ship
    # 'Win' if the attack sinks the last remaining ship
    def attack(self, x, y):
        print("Attempt to attack at location, (", x,",", y, ").")
        
        # Test that the location input is of the expected type and on the board
        if type(x) is not int or type(y) is not int:
            raise Exception("Error: This attack was not completed because the location input was not of type int.")
        if x < 0 or y < 0 or x>= self.boardWidth or y>= self.boardHeight:
            raise Exception("Error: This attack was not completed because the location input was not on the board.")
        
        #Resolve outcomes of the attack
        if self.grid[x][y] == self.hit or self.grid[x][y] == self.miss:
            print ("Already Taken! That position has previously been attacked.")
            return "Already Taken"
        elif self.grid[x][y] == self.water:
            print("Miss! No ships occupy that position.")
            self.grid[x][y] = self.miss
            return "Miss"
        else: 
            print("Hit! There is a ship occupying that position.")
            result = 'Hit'
            ship = self.ships[int(self.grid[x][y])] # grid[x][y] is the id of the ship that is hit
            ship.recordHit(x,y)
            self.grid[x][y] = self.hit
            if ship.isSunk(): #If the ship is now sunk
                print("Sunk! The attack hit the last remaining segment of a ship.")
                result = 'Sunk'
                self.numSunk += 1
                if self.numSunk == self.numShips: #That means all ships have been sunk
                    print("Win! The attack sunk the last remaining ship.")
                    result = 'Win'
            return result
    
    def randAttack(self):
        needtoAttack = True
        while needtoAttack:
            #pick random coordinates
            x = randint(0,self.boardWidth)
            y = randint(0,self.boardHeight)
        
            if grid[x][y] != self.hit or grid [x][y] != self.miss:
                outcome = attack(x,y)
                needtoAttack = False
                
            return (outcome,x,y)
    
    def nearAttack(self,x,y):
        #if near coordinates are on board and not already taken
        if x+1 < self.gridWidth and grid[x+1][y] != self.hit or grid[x+1][y] != self.miss:
            attack(x+1,y)
    
    def AI(self):
        notWin = True
        while notWin:
            (outcome,x,y) = randAttack()
            if outcome = "Hit":
                nearAttack(x,y)
            elif outcome = 'Win':
                notWin = False
                    
    # Print to stdout all information about a board including past hits, misses, and ship locations
    def __str__(self):
        return self.fullBoard()
    
    # Return all information about a board including past hits, misses, and ship locations
    def fullBoard(self):
        text = ''
        for j in range(self.boardHeight):
            for i in range(self.boardWidth):
                ch = self.grid[i][self.boardHeight-j-1]
                text += ch + ' '
            text += '\n'
        return text
    
    # Return limited information about a board including past hits and missses but not undiscovered ship locations
    def limitedBoard(self):
        text = ''
        for j in range(self.boardHeight):
            for i in range(self.boardWidth):
                ch = self.grid[i][self.boardHeight-j-1]
                if ch == self.water or ch == self.hit or ch == self.miss:
                    text += ch + ' '
                else:
                    text += self.water + ' '
            text += '\n'
        return text
    
    
    def placeShip(self,ship,shipID):
        
        if type(ship) != Ship:
            raise Exception("Error: This board could not be created because one or more inputs were of an unexpected type.")
        
        coordinates = ship.getCoordinates()
        
        # checks if all ship segments are on the board and are available.
        # Ships can't be placed on boats, hits, or misses.
        canPlaceShip = True
        for i in range(len(coordinates)):
            (x,y) = coordinates[i]
            if x<0 or y<0 or x>=self.boardWidth or y>=self.boardHeight or self.grid[x][y] != self.water: 
                canPlaceShip = False
                
        if canPlaceShip: #then place the ship on the board
            self.numShips += 1
            for i in range(len(coordinates)):
                (x,y) = coordinates[i]
                self.grid[x][y] = str(shipID)
        else:
            raise Exception("Error: This ship was not added to the board because the space was already taken.")
                
    def getWidth(self):
        return self.boardWidth
    
    def getHeight(self):
        return self.boardHeight
        
##################################################################################################################
     
        
        
        
##################################################################################################################
#### class Ship
##################################################################################################################

# A ship
class Ship:
    
    # x, y is the position of the front of the ship
    # length is the length of the ship
    # rotation is the direction of the ship ('left', 'right', 'up','down')
    def __init__(self, x,y, length, direction):
        
        #Test that the input is of the expected type and expected size.
        if type(x) is not int or type(y) is not int or type(length) is not int or type(direction) is not str:
            raise Exception("Error: The ship was not initialized because one or more inputs were of an unexpected type.")
        if length < 1: #Ships each must occupy one or more positions
            raise Exception("Error: The ship was not initialized because ships must occupy one or more positions.") 
        if direction not in ["left","right","up","down"]: 
            raise Exception("Error: The ship was not initialized because it does not have a recognized direction.")
        
        self.length = length
        self.x = x
        self.y = y
        self.direction = direction
        self.numHits = 0 #keeps track how many times a ship has been hit
         

    def getCoordinates(self):

        coordinates = []
        # initialing the coordinates list
        if self.direction == 'left':
            for i in range(self.x, self.x+self.length):
                coordinates.append((i,self.y))
        elif self.direction == 'right':
            for i in range(self.x-self.length+1, self.x+1):
                coordinates.append((i,self.y))
        elif self.direction == 'down':
            for i in range(self.y, self.y+self.length):
                coordinates.append((self.x,i))
        elif self.direction == 'up':
            for i in range(self.y-self.length+1, self.y+1):
                coordinates.append((self.x,i))
        
        return coordinates
    
    # Return true if all of the ship's coordinates have been hit, otherwise returns false
    def isSunk(self):
        if self.numHits == self.length:
            return True
        return False

    # Records a hit to the ship at a given location
    def recordHit(self, x, y):
        self.numHits += 1

##################################################################################################################





##################################################################################################################
#### play manual tests
##################################################################################################################
'''
ship1 = Ship(1,2,3,'left')
ship2 = Ship(6,7,2,'up')
ship3 = Ship(9,7,1,"right")
ship4 = Ship(0,0,1,"down")
ships = [ship1,ship2,ship3,ship4] 
board = Board(10,8,ships)
print(board)
print(board.limitedBoard())


ship1 = Ship(1,2,3,'left')
ship2 = Ship(6,7,2,'up')
ship3 = Ship(2,1,3,'down')
ship4 = Ship(5,5,4,"right")
ship5 = Ship(9,7,1,"right")
ship6 = Ship(1,0,1,"down")
ships3 = [ship1,ship2,ship4,ship5,ship6] 

board1 = Board(10,8,ships3)
print(board1)
print(board1.limitedBoard())
print(board1.fullBoard())
board1.attack(4,4)
print(board1)
board1.attack(1,2)
print(board1)
board1.attack(1,3)
print(board1.limitedBoard())
print(board1)
#board1.attack(-1,0)
'''

##################################################################################################################