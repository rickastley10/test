import random
whole = 0
while 1 == 1:
    
    
    z = input('(1) - to take a card \n (2) - to stop')
    print(whole)
    if z == '1':
        card = random.randint(1,9)
        whole = whole + card
        if whole == 21:
            print('u win')
        elif whole >= 21:
            print('u lost')
    else:
        print('error')
