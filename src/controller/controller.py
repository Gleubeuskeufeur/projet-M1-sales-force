def sortPrices(parcelle_prices):
    """
    """
    sorted_parcelle_prices = sorted(parcelle_prices, key=lambda x: x[0])
    sorted_dates = []
    sorted_prices = []
    for price_date,price in sorted_parcelle_prices:
        sorted_dates.append(price_date)
        sorted_prices.append(price)
    return sorted_dates,sorted_prices


def sortAllPrices(serialized_data):
    """
    """
    for city in serialized_data:
        for section in serialized_data[city]:
            for parcelle in serialized_data[city][section]:
                serialized_data[city][section][parcelle] = sortPrices(serialized_data[city][section][parcelle])

    return serialized_data