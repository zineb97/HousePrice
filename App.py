def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
    price = 0

    #a little pinch of this
    price += num_of_bedrooms * .841231951398213

    #and a big pinch of that
    price += sqft *1231.1231231

    #maybe a handful of this 
    price += neighborhood * 2.3242341421

    #and for good measure 
    price += 201.23432095

    return price