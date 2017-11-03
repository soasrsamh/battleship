##################################################################################################################
##################################################################################################################
###### Test Battleship
###### S.L. Howell November 2017
###### Earnest Coding Challenge 
######
###### This script does a few unit tests on the battleship.py script.
######
##################################################################################################################
##################################################################################################################



##################################################################################################################
#### Imports
##################################################################################################################
import unittest
from battleship import Board, Ship
##################################################################################################################



##################################################################################################################
#### class TestBoard
##################################################################################################################

class TestBoard(unittest.TestCase):

    #Test the attach function
    def testAttack(self):
        
        #Initialize a board
        ship1 = Ship(1,2,3,'left')
        ship2 = Ship(6,7,2,'up')
        ship3 = Ship(9,7,1,"right")
        ship4 = Ship(0,0,1,"down")
        ships = [ship1,ship2,ship3,ship4] 
        board = Board(10,8,ships)
        
        #Test that raises errors for non-int or out of range locations to the attack function
        unittest.TestCase().assertRaises(Exception, board.attack, -1, 1)
        unittest.TestCase().assertRaises(Exception, board.attack, 1, -1)
        unittest.TestCase().assertRaises(Exception, board.attack, 100, 1)
        unittest.TestCase().assertRaises(Exception, board.attack, 1, 100)
        unittest.TestCase().assertRaises(Exception, board.attack, 1.2, 1)
        unittest.TestCase().assertRaises(Exception, board.attack, 1, 1.2)
        unittest.TestCase().assertRaises(Exception, board.attack, "1", 1)
        unittest.TestCase().assertRaises(Exception, board.attack, 1, "1")
        unittest.TestCase().assertRaises(Exception, board.attack, [1], 1)
        unittest.TestCase().assertRaises(Exception, board.attack, 1, [1])
        
        #Test 'Hit'
        a = board.attack(1,2)
        unittest.TestCase().assertEqual(a, 'Hit')
        fullBoard = \
        "W W W W W W 1 W W 2 \n"+ \
        "W W W W W W 1 W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X 0 0 W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "3 W W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
        
        #Test 'Miss'
        a = board.attack(1,0)
        unittest.TestCase().assertEqual(a, 'Miss')
        fullBoard = \
        "W W W W W W 1 W W 2 \n"+ \
        "W W W W W W 1 W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X 0 0 W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "3 M W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
        
        #Test 'Already Taken' 
        a = board.attack(1,2)
        b = board.attack(1,0)
        unittest.TestCase().assertEqual(a, 'Already Taken')
        unittest.TestCase().assertEqual(b, 'Already Taken')
        fullBoard = \
        "W W W W W W 1 W W 2 \n"+ \
        "W W W W W W 1 W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X 0 0 W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "3 M W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
        
        #Test 'Sunk' 
        a = board.attack(2,2)
        b = board.attack(3,2)
        unittest.TestCase().assertEqual(a, 'Hit')
        unittest.TestCase().assertEqual(b, 'Sunk')
        fullBoard = \
        "W W W W W W 1 W W 2 \n"+ \
        "W W W W W W 1 W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X X X W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "3 M W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
        
        #Test 'Win' 
        a = board.attack(6,6)
        b = board.attack(6,7)
        c = board.attack(9,7)
        d = board.attack(0,0)
        unittest.TestCase().assertEqual(a, 'Hit')
        unittest.TestCase().assertEqual(b, 'Sunk')
        unittest.TestCase().assertEqual(c, 'Sunk')
        unittest.TestCase().assertEqual(d, 'Win')
        fullBoard = \
        "W W W W W W X W W X \n"+ \
        "W W W W W W X W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X X X W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "X M W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
        
    #Test the print output
    def testOutput(self):
        
        #Initialize a board
        ship1 = Ship(1,2,3,'left')
        ship2 = Ship(6,7,2,'up')
        ship3 = Ship(9,7,1,"right")
        ship4 = Ship(0,0,1,"down")
        ships = [ship1,ship2,ship3,ship4] 
        board = Board(10,8,ships)
        
        #Test board size
        unittest.TestCase().assertEqual(board.getWidth(), 10)
        unittest.TestCase().assertEqual(board.getHeight(), 8)
        
        #Test limited board output and full board output initially
        limitedBoard = \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"
        fullBoard = \
        "W W W W W W 1 W W 2 \n"+ \
        "W W W W W W 1 W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W 0 0 0 W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "3 W W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.limitedBoard(), limitedBoard)
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
        
        #Test limited board output and full board output after attacks
        a = board.attack(1,2)
        a = board.attack(1,0)
        limitedBoard = \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W M W W W W W W W W \n"
        fullBoard = \
        "W W W W W W 1 W W 2 \n"+ \
        "W W W W W W 1 W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "W X 0 0 W W W W W W \n"+ \
        "W W W W W W W W W W \n"+ \
        "3 M W W W W W W W W \n"
        unittest.TestCase().assertEqual(board.limitedBoard(), limitedBoard)
        unittest.TestCase().assertEqual(board.fullBoard(), fullBoard)
##################################################################################################################

    
    
##################################################################################################################
#### Run tests
##################################################################################################################
  
if __name__ == '__main__':
    unittest.main()
    
##################################################################################################################


        #unittest.TestCase().assertTrue(expression)
        #unittest.TestCase().assertFalse(expression)
        #unittest.TestCase().assertEqual(expected, expression)
        #unittest.TestCase().assertRaises(error, *args)
