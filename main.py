import Controller.VendingMachineController as Controller
app = Controller.VendingMachineController()

while 1:
    # Intro & drink selection
    selection = app.index()

    # Internal processing
    drink = app.get_drink(selection)

    # Payment View
    payment = app.pay_drink(drink)

    # Internal processing
    app.add_to_cash_register(payment)
    app.remove_drink(drink)
    print("[ADMINLOG]: In der Kasse befinden sich nun: %.2f€." %(app.get_cash_register()))