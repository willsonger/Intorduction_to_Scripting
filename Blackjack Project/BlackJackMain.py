from elements import *

def game_start(rounds):
    '''
    Pregame first Round: Random numbers of decks between 2 and 8 are shuffled 
    and placed in shoe.
    Random number of players: Between 1 and 6 players
    
    '''
    
    x=random.randint(4, 8)      
    shoe = CardShoe(x)
    dealer = Dealer()
    num_ppl = random.randint(1, 6)
    print("There will be", num_ppl, "players playing 10 rounds" )
    
    player_list = []
    for i in range(int(num_ppl)):
        name = 'Player' + str(i + 1)
        player = Player(name)
        player_list.append(player)
        
    ### 10 rounds/games
    for i in range(rounds):
        print()
        print('*************** Game {} ***************'.format(i+1))
        
        enough_money_players = []
        for player in player_list:
            if player.get_chips() >= 50:
                enough_money_players.append(player)
                
        # reset everything for each player
        for player in enough_money_players:
            bets = random.randint(25, player.get_chips() -1)
            player.set_bets(bets)
            player.reset_cards()
            print(player.get_name(), 'bets $', player.get_bets())
    
        dealer.reset_cards()
    
        print('=============== 1st hand ===============')
        for player in enough_money_players:
            new_card = shoe.deal()
            player.add_card(new_card)
            player.faceup_display()
            
        new_card = shoe.deal()
        dealer.add_card(new_card)
        dealer.facedown_display()
        
        print('=============== 2nd hand ===============')
        for player in enough_money_players:
            new_card = shoe.deal()
            player.add_card(new_card)
            player.faceup_display()
            
        new_card = shoe.deal()
        dealer.add_card(new_card)
        dealer.facedown_display()
        
        '''this hand is where the dealer can hit after players are done hitting or standing.
        players will hit until there hand is over 17.
            This hand also varifies the number of players left in the game. 
        '''
        print('=============== next hand ===============')
        while 1:
            ready_count = 0
            for player in enough_money_players:
                if player.get_status() in 'below17':
                    new_card = shoe.deal()
                    player.add_card(new_card)
                    player.faceup_display()
                else:
                    ready_count += 1
                    
                    
            if ready_count == len(enough_money_players):
                break
            else:
                print('=============== next hand ===============')
        '''
        This hand is played after all players determins if the player is bust 
        Dealer shows his facedown new_card unless all players are bust. then new 
        hand begins without showing his facedown card
        
        '''
        print("    (Dealer's hand)")
        ### check if all players got bust
        bust_count = 0
        for player in enough_money_players:
            if player.get_status() == 'bust':
                bust_count += 1
        
        if bust_count != len(enough_money_players):
            dealer.faceup_display()
            while 1:
                if dealer.get_status() == 'below17':
                    new_card = shoe.deal()
                    dealer.add_card(new_card)
                    dealer.faceup_display()
                else:
                    break
            
        print("=============== Money paid or collected ===============")
        '''
        This is end of round or game and Dealer determins who has won 
        and all bets are paid out. for either bust, blackjack, above 17 
        or below 17. bets are paid out at a 2:1 for a hard win and 3;1 FOR BLACKJACK
        players winings or lose is added or subtracted from their bank. 
        '''
        dealer_total = dealer.get_sum()
        if dealer.get_status() == 'bust':
            dealer_total = 0
        for player in enough_money_players:
            player_total = player.get_sum()
            # consider bust as 0
            
            if player.get_status() == 'bust':
                player_total = 0
                
            # comparison
            if dealer_total > player_total:
                money = player.get_bets()
                dealer.add_chips(money)
                player.add_chips(-money)
                msg = '{} loses by ${}. ({} has ${}, dealer has ${})'.format(
                    player.get_name(), player.get_bets(), player.get_name(), 
                    player.get_chips(), dealer.get_chips())
                print(msg)
            elif player_total > dealer_total:
                money = player.get_bets()
                if player.get_status() == 'blackjack':
                    money = money * 3
                else:
                    money = money * 2
                dealer.add_chips(-money)
                player.add_chips(money)
                msg = '{} wins by ${}. ({} has ${}, dealer has ${})'.format(
                    player.get_name(), money, player.get_name(), 
                    player.get_chips(), dealer.get_chips())
                print(msg)


game_start(10)

while True:
    print()
    ans = input("How many more rounds you want to play ? (0 for quit) ")
    try:
        rounds = int(ans)
        if rounds == 0:
            print('bye!')
            break
            sys.exit()
        game_start(rounds)
    except Exception as e:
        print('Things went wrong', e)
        
