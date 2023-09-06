import time
import random
print('Welcome to ripoff Blackjack.')
time.sleep(1.5)
deck = ['sA','s2','s3','s4','s5','s6','s7','s8','s9','s10','sJ','sQ','sK','hA','h2','h3','h4','h5','h6','h7','h8','h9','h10','hJ','hQ','hK','cA','c2','c3','c4','c5','c6','c7','c8','c9','c10','cJ','cQ','cK','dA','d2','d3','d4','d5','d6','d7','d8','d9','d10','dJ','dQ','dK']
while True:#i was really tired of the messages overe and over so i made it
            try:#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
               
                skip=str(input("Skip?(y/n)"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                #we're ready to exit the loop.
                break
if skip=='y':
    print('Skipped')
else:
    print('Whether the ripoff is the code or the luck of the dealer,')
    time.sleep(2)
    print("It's time to find out")
    time.sleep(2)
    print("It's not entirely accurate but it works so...")
    time.sleep(0.5)
    print('For verification, here is the deck')
    time.sleep(2)
    print(deck)
    time.sleep(2)
nextcard=52
dealer=['empty']
player=['empty']
dealerVal=0
playerVal=0
stand = 'false'
ace=11
gameState=0
played=0
def reset():#for infinite playing
    global playerVal, player, nextcard, deck
    global dealerVal, gameState, stand, dealer
    random.shuffle(deck)#you won't find any cheap tricks in here
    print('Shuffling')
    lasttenth= deck[-10]#not impimented yet
    nextcard=52
    dealer=['empty']
    player=['empty']
    dealerVal=0
    playerVal=0
    gameState=0
    time.sleep(3)
    stand = 'false'
    if played>10:
        print('''We like playing blackjack, but we like fresh air too!
Get some fresh air and take a break if you've played too long.''')
    play()
    
def playagain():
    while True:
            try:
                goon=str(input("Play Again?(y/n)"))#go on
            except ValueError:
                print("Sorry, I didn't understand that.(Has to be uppercase)")
                continue
            
            else:
                #we're ready to exit the loop.
                break
            
    if goon=='y':
        reset()
        
    else:
        print('Thanks for playing, Come again!')
        exit()
        print('Please exit.')
        time.sleep(2)
        exit()
        print('Whatever happens from here is your fault')
        exit()
        print('Not mine.')
        exit()
        return()

        
def usecard(uses):#deck[-nextcard] gives the next card for use
    global nextcard
    nextcard=nextcard-1
    
def win():
    global gameState, played
    played=played+1
    gameState=1
    print('You Won!')
    playagain()

def loss():
    global gameState, played
    played=played+1
    gameState=2
    print('You Loss')
    playagain()

def deckSums(inputCard,sourcecheck):#checks all values before aces, force ace because i can't be bothered to make the 11 or 1 logistics that complicated.
    global playerVal, dealerVal
    if inputCard=='sK' or inputCard=='cK' or inputCard=='hK' or inputCard=='dK'or inputCard=='sQ'or inputCard=='cQ' or inputCard=='hQ' or inputCard=='dQ' or inputCard=='sJ' or inputCard== 'cJ' or inputCard== 'hJ' or inputCard=='dJ' or inputCard=='s10' or inputCard=='c10' or inputCard=='h10' or inputCard=='d10':
        if sourcecheck == 0:
            playerVal=playerVal+10
        elif sourcecheck == 1:
            dealerVal=dealerVal+10
    if inputCard=='s2' or inputCard=='c2' or inputCard=='h2' or inputCard=='d2':
        if sourcecheck == 0:
            playerVal=playerVal+2
        elif sourcecheck == 1:
            dealerVal=dealerVal+2
    if inputCard=='s3' or inputCard=='c3' or inputCard=='h3' or inputCard=='d3':
        if sourcecheck == 0:
            
            playerVal=playerVal+3
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+3
    if inputCard=='s4' or inputCard=='c4' or inputCard=='h4' or inputCard=='d4':
        if sourcecheck == 0:
            
            playerVal=playerVal+4
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+4
    if inputCard=='s5' or inputCard=='c5' or inputCard=='h5' or inputCard=='d5':
        if sourcecheck == 0:
            
            playerVal=playerVal+5
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+5
    if inputCard=='s6' or inputCard=='c6' or inputCard=='h6' or inputCard=='d6':
       
        if sourcecheck == 0:
            
            playerVal=playerVal+6
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+6
    if inputCard=='s7' or inputCard=='c7' or inputCard=='h7' or inputCard=='d7':
        if sourcecheck == 0:
            
            playerVal=playerVal+7
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+7
    if inputCard=='s8' or inputCard=='c8' or inputCard=='h8' or inputCard=='d8':
        if sourcecheck == 0:
            
            playerVal=playerVal+8
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+8
    if inputCard=='s9' or inputCard=='c9' or inputCard=='h9' or inputCard=='d9':
        if sourcecheck == 0:

            playerVal=playerVal+9
        elif sourcecheck == 1:
            
            dealerVal=dealerVal+9
    if inputCard=='sA' or inputCard=='cA' or inputCard=='hA' or inputCard=='dA':
        if sourcecheck == 0:
            if playerVal+11<=21:
                playerVal=playerVal+11
                
            elif playerVal+11>21:
                playerVal=playerVal+1
                
        elif sourcecheck == 1:
            if dealerVal+11<=21:
                dealerVal=dealerVal+11
                
            elif dealerVal+1>21:
                dealerVal=dealerVal+1

                
def valuecheck(optioncheck):#sets up decksums and checks win conditions
    #check win or loss
    global playerVal, dealerVal
    if optioncheck==0:#player decksums setup
        playerVal=0
        for value in range(0,len(player)):

            deckSums(player[value],0)
            
    if optioncheck==1:#dealer decksums setup
        dealerVal=0
        for value in range(0,len(dealer)):

            deckSums(dealer[value],1)
            
    if playerVal > 21:#game end conditions
        print('Player Bust')
        loss()
        
    elif dealerVal > 21 and stand == 'true':
        print('Dealer Bust')
        win()
        
    elif dealerVal==playerVal and playerVal>=17 and stand=='true':
        print('Tie')
        playagain()
        
    elif dealerVal==21 and playerVal<21 and stand == 'true':
        print('Dealer Wins!')
        loss()
        
    elif playerVal==21 and dealerVal<21 and stand == 'true':
        print('Player Wins!')
        win()
        
    elif playerVal<dealerVal and stand == 'true':
        print('Dealer Wins!')
        loss()
        
    elif dealerVal<playerVal and stand == 'true':
        print('Player Wins!')
        win()
        
    elif optioncheck=='0':#because it'll give an double message without the condition
        print('Next Turn')#cuz i run it individually for dealer and player


def play():
    global player, dealer
    global playerVal, stand, dealerVal
    time.sleep(2)
    playing= 'y'
    print('Dealing Cards')
    time.sleep(2)
    player= [deck[-nextcard]]
    usecard(1)
    player.append(deck[-nextcard])
    usecard(1)
    print('You have', player)
    dealer=[deck[-nextcard],deck[-(nextcard-1)]]
    usecard(2)
    valuecheck(0)#player check
    valuecheck(1)#dealer check
    print('Dealer has',dealer[0],',hidden')
    if playing== 'y':#second round and more
        
        while playing=='y':
            
            while True:#forced input
                move= input("Hit or Stand")#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
                if (move!='Hit') and (move!='Stand') :#for whatever reason only this combination seems to work.
                    print("Sorry, I didn't understand that.")

                else:
                    if move=='Stand' or move=='Hit':
                        if move=='Hit':#hit deck
                            time.sleep(1)
                            playing= 'y'
                            print('Dealing Card')
                            time.sleep(1)
                            player.append(deck[-nextcard])
                            usecard(1)
                            print('You have', player)
                            valuecheck(0)
                            
                        elif move=='Stand':#stand
                            valuecheck(1)
                            print('Dealer has', dealer)
                            while dealerVal<=17:
                                print('Dealer drawing card')
                                time.sleep(2)
                                dealer.append(deck[-nextcard])
                                usecard(1)
                                valuecheck(1)
                                print('Dealer Has', dealer)
                                
                                if dealerVal>=17:
                                    break
                            
                            if dealerVal>=17:#works if starts whether >=17 or it needs to get biggre
                                stand = 'true'
                                valuecheck(0)
                                valuecheck(1)
                                break
                break
          
reset()
print('Now Shuffling the deck...')
play()


            




