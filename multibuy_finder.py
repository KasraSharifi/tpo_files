def multibuy_finder(promo_tag):
    if promo_tag.find("WYB") >= 0:
        print("MustBuy")
    elif promo_tag.find("/$"):
        print("MustBuy")
    else:
        print("Temporary Price Reduction")

