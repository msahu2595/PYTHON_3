# Exception handeling
# try except else finally


while True:
    try:
        age = int(input('enter your age: '))
        break
    except ValueError:
        print("maybe you entered string instead of number, try again")
    except:
        print('invalid input')


# age =  int(input('enter your age: '))

if age < 18:
    print('you can\'t play this game.')
else:
    print('you can paly this game...')

    


