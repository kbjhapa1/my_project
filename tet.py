#This is a class program that prints a rank, suits,Blackjack value of the card, and name of the card.


class Card: #Defining a Card class that stores rank and suit of a card and stores getRank, getSuit, BJValue and special string method.
   suits = {"s": "Spades", "d": "Diamonds", "c": "Clubs", "h": "Hearts"} # A class variable that stores suits

   def __init__(self, rank, suit = 0):
       #Defining init function (constructor) that indicates rank from 1-13 as well as the card's suit and It executes everytime an object is created .
       self.rank = rank
       self.ranks = [None,'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # Instance variable of a Card class.
       self.suit = suit

       if type(self.rank) != int:
        raise TypeError()

       if type(self.suit)!= str:
        raise TypeError()

       '''if self.ranks !=[None,'Ace', '2', 3, '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
        raise ValueError()

       if self.suit != 's' or 'd' or 'c' or 'h':
        raise ValueError()

        if self.suit != 's' or 'd' or 'c' or 'h':
        raise ValueError()'''

   def getRank(self): #This function returns the rank of the card.
       return self.rank  

   def getSuit(self): #This function returns the suit of the card.
       return self.suits[self.suit]

   def BJValue(self): #This function returns the Blackjack value of the card.
      return self.rank

   def __str__(self): #Returns a string that names the card.
       return "%s of %s." % (self.ranks[self.rank], self.suits[self.suit])

# Testing of the program.
try:
	playingCard= Card(1, 's') #Creating an object playingcard of a class Card.
	print(playingCard) #This prints object from str method.
	print (playingCard.getRank()) #Calling getRank method.
	print(playingCard.getSuit()) #Calling getSuit method.
	print(playingCard.BJValue())#Calling BJValue method.
  	
except:
  	print('The first parameter must be an integer.') #This block of code executes when the first argument is not an integer.

except:
	print('The second parameter must be a string.')
  	
'''except ValueError:
  print('The value of first parameter does not belongs to rank.')

except ValueError:
  print("The value of the second parameter is not one of the strings in the set 's', 'h', 'c', 'd'")'''




"""
   Ace of Clubs
   1
   Clubs
   Ace

"""



































