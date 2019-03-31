# else and finally clause in exception handling


while True:
    try:
        number = int(input('enter your number: '))
    except ValueError:
        print("Plese type integer")
    except:
        print('Unexpected error')
    else:
        print(f"userinput = {number}")
        break
    finally:
        print('finally block...............')





