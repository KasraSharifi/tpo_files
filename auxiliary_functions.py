def outlier_finder(prices_list, max_price):
    for price in prices_list:
        if price > max_price:
            print(f"we have a price that is unusuaaly big and the price is {price}")