print("What's the total price of the Goods, you bought")
total_price_of_goods = int(input())

if total_price_of_goods >= 30000 and total_price_of_goods < 50000:
    print("Congratlation!! You just won a refrigerator")
elif total_price_of_goods >= 50000 and total_price_of_goods < 100000:
    print("Congratulations You've just won a Genertor")
elif total_price_of_goods >= 100000:
    print("Congratulations!! YOU've Just won a car")
else:
    print("Shop more, to get a gift item.")
