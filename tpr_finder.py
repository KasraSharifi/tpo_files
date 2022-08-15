def tpr_finder(promo_tag):
    if (promo_tag.find("WYB") < 0) and (promo_tag.find("/$") < 0):
        print("Temporary Price Reduction") 