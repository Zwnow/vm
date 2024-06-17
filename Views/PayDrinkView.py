def PayDrinkView(drink):
    total_payment = 0
    while total_payment < drink.price:
        try:
            current_payment = round(float(input("Moneten bitte, Restbetrag: %.2f€: " %(drink.price - total_payment))), 2)
            if current_payment > 0:
                total_payment += current_payment
        except:
            print("Bitte zahlen Sie einen gültigen Betrag!")
            if total_payment > 0:
                print("*Der Automat spuckt %.2f€ aus.*" %(total_payment))
            quit()
    
    print("*Der Automat spuckt %s und %.2f€ Wechselgeld aus.*" %(drink.name, total_payment - drink.price))

    return total_payment - (total_payment - drink.price)