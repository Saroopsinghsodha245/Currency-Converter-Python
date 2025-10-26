def currency_converter():
    def usd(pkr):
        return pkr / 281

    def eur(pkr):
        return pkr / 330

    def inr(pkr):
        return pkr / 3.17

    def jpy(pkr):
        return pkr / 1.91

    def sar(pkr):
        return pkr / 75
    print("Pakistan Currency Converter")

    print("Select currency to convert PKR into:")
    print("1. USD")
    print("2. EUR")
    print("3. INR")
    print("4. JPY")
    print("5. SAR")

    choice = int(input("Enter your choice in currency: "))
    amount = float(input("Enter amount in PKR: "))

    if choice == 1:
        print(amount, "PKR =", usd(amount), "USD")
    elif choice == 2:
        print(amount, "PKR =", eur(amount), "EUR")
    elif choice == 3:
        print(amount, "PKR =", inr(amount), "INR")
    elif choice == 4:
        print(amount, "PKR =", jpy(amount), "JPY")
    elif choice == 5:
        print(amount, "PKR =", sar(amount), "SAR")
    else:
        print("Invalid input!")

currency_converter()
