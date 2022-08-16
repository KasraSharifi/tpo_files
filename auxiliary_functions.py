def outlier_finder(prices_list, max_price):
    for price in prices_list:
        if price > max_price:
            print(f"we have a price that is unusuaaly big and the price is {price}")


def eq_to_litres(eq_value):
    litres_value = eq_value * 5.6


def input_file_leaning(input_file):
    input_file.loc[input_file["volume"] < 0, "volume"] = 0