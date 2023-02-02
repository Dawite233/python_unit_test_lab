def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

   ## Add validation to make sure that list contain ints and list does not contain strings || float

    if len(item_prices) >= 3:
        item_prices.sort()
        return item_prices[0]
    else:
        return None

if __name__ == '__main__':
    main()