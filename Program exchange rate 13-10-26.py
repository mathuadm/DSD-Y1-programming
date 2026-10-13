#Program exchange rate(searched up rounding code to 2 decimaclnumber)

yen = float(209.19)
euro = float(1.18)
dollar = float(1.32)
pound = float(1)

currency = input("what currency do you wish to exchange? ")
if currency == "yen":
    print("you have choice to exchange your yen ")
    currencyp2 = input("what do you what your currency into ")
    if currencyp2 == "euro":
        print("you have chosen to exchange your yen in euro ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(yen)) * float(euro))
        roundcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "dollar":
        print("you have chosen to exchange your yen in dollar ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(yen)) * float(dollar))
        print(newcur)
    elif currencyp2 == "pound":
        print("you have chosen to exchange your yen in pound ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(yen)))
        roundcur = round(newcur,2)
        print(roundcur)
    else:
        print("that is not an available currency to exchange")
elif currency == "euro":
    print("you have choice to exchange your euro ")
    currencyp2 = input("what do you what your currency into ")
    if currencyp2 == "yen":
        print("you have chosen to exchange your euro into yen ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(euro)) * float(yen))
        roundcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "dollar":
        print("you have chosen to exchange your euro in dollar ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(euro)) * float(dollar))
        roundcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "pound":
        print("you have chosen to exchange your euro in pound ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(euro)))
        roundcur = round(newcur,2)
        print(roundcur)
    else:
        print("that is not an available currency to exchange")    
elif currency == "dollar":
    print("you have choice to exchange your dollar ")
    currencyp2 = input("what do you what your currency into  ")
    if currencyp2 == "yen":
        print("you have chosen to exchange your dollar in yen ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(dollar)) * float(yen))
        roundcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "euro":
        print("you have chosen to exchange your dollar in euro ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(dollar)) * float(euro))
        newcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "pound":
        print("you have chosen to exchange your dollar in pound ")
        money = input("how much do you have to exchange? ")
        newcur = ((float(money) / float(dollar)))
        roundcur = round(newcur,2)
        print(roundcur)
    else:
        print("that is not an available currency to exchange")
elif currency == "pound":
    print("you have choice to exchange your pound ")
    currencyp2 = input("what do you what your currency into ")
    if currencyp2 == "yen":
        print("you have chosen to exchange your pound into yen ")
        money = input("how much do you have to exchange? ")
        newcur = (float(money) * float(yen))
        roundcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "euro":
        print("you have chosen to exchange your pound into euro")
        money = input("how much do you have to exchange? ")
        newcur = (float(money) * float(euro))
        roundcur = round(newcur,2)
        print(roundcur)
    elif currencyp2 == "pound":
        print("you have chosen to exchange your pound into dollar ")
        money = input("how much do you have to exchange? ")
        newcur = (float(money) * float(dollar))
        roundcur = round(newcur,2)
        print(roundcur)
    else:
        print("that is not an available currency to exchange")        
else:
    print("you cannot exchange that.")
