import random

think = 'true' # Lines 3 and 4 run the while loop. 
feel = 'true' 

# The prize pool where gachapon() gets its results from. 
Banner_pool = {'Common': {
                1: 'Salmon Sashimi',
                2: 'Tuna Sashimi',
                3: 'Shrimp Sashimi',
                4: 'Egg Sashimi',
                5: 'Mackeral Sashimi'}, 
                'Rare':{
                1: 'California Roll', 
                2: 'Lemon Roll'},
                'Epic':{
                1: 'Dragon Roll',
                2: 'Tokyo Dynamite Roll'}}
                
# Rarity list. 'Common' isn't in order with the others to make sure that 1 through 3 isn't frontloaded to being just 'Common'. 
rarity = ['Common', 'Common', 'Rare', 'Rare', 'Common', 'Epic']

# Inventory of the machine. 

total_inven = 30

# Interaction with the user after they've acquired their first prize. 
def decision2():
    while (feel == 'true'):
        decision_two = input()
        if decision_two == 'Y' or decision_two == 'y' or decision_two == 'Yes' or decision_two == 'YES' or decision_two == 'yes':
            gachapon()
        elif decision_two == 'N' or decision_two == 'n' or decision_two == 'No' or decision_two == 'NO' or decision_two == 'no':
            print ('You stand up and look at all your prize(s) in your bag. You walk home feeling satisfied.')
            exit()
        elif decision_two != 'Y' or decision_two != 'Yes' or decision_two != 'YES' or decision_two != 'yes' or decision_two != 'N' or decision_two != 'No' or decision_two != 'NO' or decision_two != 'no':
            print (f'\'{decision_two}\' is not a supported option.')
            print ('Would you like to insert another coin? Y/N')

# The gachapon machine. The function first chooses the rarity, and then a random number is selected based on the rarity to choose a specific prize from the dict.
# Ex., rarity_picker chooses 'Common,' and then num1 gets '4'. The prize will be 'Egg Sashimi'. 
def gachapon():
    global total_inven # Lines 44 - 47 is ran when the machine's inventory is empty. 
    if total_inven == 0:
        print ('You look into the machine and realize that it is out of prizes.')
        print ('You look into your bag and realize that you have 30 capsules! Too many for one person. You walk home satisfied, albeit, with your bag feeling heavier than before.')
        exit()
    rarity_picker = random.choice(rarity)
    num1 = random.randint(1,5) 
    num2 = random.randint(1,2)
    if rarity_picker == 'Common':
        prize1 = Banner_pool[rarity_picker][num1] # <--  Determines what prize is given. Is ran based on the specific rarity.
        total_inven -= 1 
        print(f'Congratulations, you\'ve received a common \'{prize1}\'. {total_inven} prizes remain.')
        print ('Would you like to insert another coin?')
        decision2()
    elif rarity_picker == 'Rare':
        prize2 = Banner_pool[rarity_picker][num2]
        total_inven -= 1
        print(f'Congratulations, you\'ve received a rare \'{prize2}\'. {total_inven} prizes remain.')
        print ('Would you like to insert another coin?')
        decision2()
    elif rarity_picker == 'Epic':
        prize3 = Banner_pool[rarity_picker][num2]
        total_inven -= 1
        print(f'Congratulations, you\'ve received a epic \'{prize3}\'. {total_inven} prizes remain.')
        print ('Would you like to insert another coin?')
        decision2()

# The first decision when starting up the program. Is built to continue looping if replied "No" or anything other than "Yes" or its other accepted inputs. 
def decision1():
    while (think == 'true'):
        print ('Would you like to insert a coin to acquire a prize? Y/N')
        decision = input()
        if decision == 'Y' or decision == 'y' or decision == 'Yes' or decision == 'YES' or decision == 'yes':
            gachapon()
        elif decision == 'N' or decision == 'n' or decision == 'No' or decision == 'NO' or decision == 'no':
            print ('You second guess your decision, you ask yourself that question again.')
        elif decision != 'Y' or decision != 'Yes' or decision != 'YES' or decision != 'yes' or decision != 'N' or decision != 'No' or decision != 'NO' or decision != 'no':
            print (f'\'{decision}\' is not a supported option.')
    
print ('You\'ve stumbled upon a gachapon machine on your walk home. You kneel down to the machine to see the prize selection.')
print ('The prizes are all sushi-themed keychains! This very much interests you, so you think to yourself...')
decision1()









    




