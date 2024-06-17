def IndexView(drinks):
    print('Hi, welches Getränk hätten Sie gern?')
    for drink in drinks:
        print(drink.__str__())
    try:
        return int(input())
    except:
        print("Bitte geben Sie eine gültige Zahl an.")
        quit()