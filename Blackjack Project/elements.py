'''
Here are the basi elements needed to play a game of Blackjack
1. deck of cards randomaly shuffled
2. a Card shoe class which holds muliple decks of cards and reshuffles them once
   all the decks are placed in the shoe.
3. a player class with private variables and various funtions needed to play
   the game. 
4. A dealer class with private variables and funtions needed to play the game.
5. there are brief discriptions above each class and funtion within the class
   to help understand the structural logic of my code

'''

import random
'''
Rank is the library that holds the key and the value of each card.
each card is assigned to a specific suite within the deck using the
traditional symboles of club, diamond, heart and spade in the get_one_deck
in the for loop. Once this is completted the deck is randomly shuffeled for
each deck that is randomly drawn. 
'''

RANK = { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
         '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,'K': 10,}

def get_one_deck():
    deck = []
    for i in RANK.keys():
        #for j in ['X', 'Y', 'Z', 'S']:
        for j in ['♣', '♦', '♥', '♠']:
            symbol = i + ' ' + j
            deck.append(symbol)
            
    # shuffle in deck
    random.shuffle(deck)
    #print("random shuffle of decks of cards", deck)
    
    return deck
'''
Here I've created a card shoe class with the private varaibles index and cards
which index the cards that have been shullfed both outside of being placed
within the shoe and once again inside of the shoe. As per requested by the professor
I have included a write to file feature so that my indexing can be verified to
be randomly shuffled and delt accordingly to the shuffle. I have also included within
the shoe class a deal funtion which indexs the cards as thev are being delt to each
player. 
'''
class CardShoe:
    def __init__(self, decks):
        # private members
        self.__index = 0
        self.__cards = []
        
        for n in range(decks):
            for symbol in get_one_deck():
                self.__cards.append(symbol)
                
        #shuffle in shoe
        random.shuffle(self.__cards)
        #print(len(self.__cards))
        #print("Random Shuffle of shoe of cards", (self.__cards))
        

        #write random shuffle to a text file. 
        file_name = 'cards.txt'
        with open(file_name, 'w', encoding='utf-8') as f:
            for card in self.__cards:
                row = '{}\n'.format(card)
                f.write(row)

    def deal(self):
        card = self.__cards[self.__index]
        self.__index += 1
        return card
'''
Player Class is made up of several private variables: players name,
cards, bets, and chips. It also containf several funtions which are
needed to simulate a player playing a game of Blackjack.  
'''
############ Player Class #############
## keeps track of cards, bets, chips## 
class Player:
    def __init__(self, name):
        # private members
        self.__name = name
        self.__cards = []
        self.__bets = 0
        self.__chips = random.randint(500, 5000)
        
        print(self.__name, ", your bank is: $", self.__chips)
        
    def get_name(self):
        return self.__name
    
    # setter and getter for bets
    def get_bets(self):
        return self.__bets
    
    def set_bets(self, bets):
        self.__bets = bets    
    
    # setter for chips
    def get_chips(self):
        return self.__chips
    
    # when the player wins or loses
    def add_chips(self, chips):
        self.__chips += chips
    
    def add_card(self, card):
        self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    def reset_cards(self):
        self.__cards = []
# Gets the sum of card
    def get_sum(self):
        has_ace = False
        total = 0
        for symbol in self.__cards:
            key, suit = symbol.split(' ')
            if key == 'A':
                has_ace = True
            num = RANK[key]
            total += num
        
        if has_ace and 0:
            total += 10
            
        return total

    def get_status(self):
        has_ace = False
        total = 0
        for symbol in self.__cards:
            key, suit = symbol.split(' ')
            if key == 'A':
                has_ace = True
            num = RANK[key]
            total += num

        if total > 21:
            return 'bust'
        elif not has_ace and total == 21:
            return 'blackjack'
        elif has_ace and (total+10) == 21:
            return 'blackjack'
        elif has_ace and (total+10) >= 17:
            return 'above17'
        elif total >= 17:
            return 'above17'
        else:
            return 'below17'

    def faceup_display(self):
        hands_total = self.get_sum()
        note = ''
        if hands_total > 21:
            note = '(bust)'
        elif hands_total == 21:
            note = '(blackjack)'
        elif 17 <= hands_total < 21:
            note = '(final hand value)'.format()
        msg = '{}: cards= {}, sum = {} {}'.format(
            self.__name, self.get_cards(), hands_total, note)
        print(msg)    
            
########## Dealer ##############  
class Dealer:
    def __init__(self):
        # private members
        self.__name = "Dealer"
        self.__cards = []
        self.__chips = 500000

    def get_name(self):
        return self.__name

    # getter for chips
    def get_chips(self):
        return self.__chips
    
    # when the player wins or loses
    def add_chips(self, chips):
        self.__chips += chips
        
    def add_card(self, card):
        self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    def reset_cards(self):
        self.__cards = []
        
    def get_sum(self):
        has_ace = False
        total = 0
        for symbol in self.__cards:
            key, suit = symbol.split(' ')
            if key == 'A':
                has_ace = True
            num = RANK[key]
            total += num
        
        if has_ace and 0:
            total += 10
            
        return total
    
    def get_status(self):
        has_ace = False
        total = 0
        for symbol in self.__cards:
            key, suit = symbol.split(' ')
            if key == 'A':
                has_ace = True
            num = RANK[key]
            total += num

        if total > 21:
            return 'bust'
        elif not has_ace and total == 21:
            return 'blackjack'
        elif has_ace and (total+10) == 21:
            return 'blackjack'
        elif has_ace and (total+10) >= 17:
            return 'above17'
        elif total >= 17:
            return 'above17'
        else:
            return 'below17'
            
    def faceup_display(self):
        hands_total = self.get_sum()
        note = ''
        if hands_total > 21:
            note = '(bust)'
        elif hands_total == 21:
            note = '(blackjack)'
        elif 17 <= hands_total < 21:
            note = '(final hand value)'
        msg = '{}: cards= {}, sum = {} {}'.format(
            self.__name, self.get_cards(), hands_total, note)
        print(msg)
        
    def facedown_display(self):
        cards = list(self.get_cards())
        cards[0] = 'FaceDown'
        msg = '{}: cards= {}'.format(self.__name, cards)
        print(msg)
        
