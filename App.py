def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
    price = 0

    #in my area the average house costs $200 per sqft
    price_per_sqft = 200

    if neighborhood == "hipsterton":
        price_per_sqft = 400

    elif neighborhood == "skid row":
        price_per_sqft =100

    #start with a base price estimate based on how big the place is
    price = price_per_sqft * sqft

    #now adjust the our estimate based on the number of the bedrooms
    if num_of_bedrooms ==0:
        price = price -20000
    else:
        price = price + (num_of_bedrooms * 1000)

    return price