def Guess_the_number():
    print('guess the number between 1 to 100')
    random_number = 35
    found = False
    
    try:
        while not found:
            user_guess = int(input('guess the number:'))
            if user_guess == random_number:
                print('you are correct...' ,' congrats!')
                found = True
            elif user_guess > random_number:
                print('guess the lower number')
        
            else:
                print('guess the higer number')
    except:
        print('enter the valid number')
        print('Try again.....#')
    
Guess_the_number()
