def MaximumDiscount(N, price):
    if len(price) < 3:
        return 0

    price.sort()
    price.reverse()

    discount = 0
    for i in range(2, len(price), 3):
        discount += price[i]

    return discount
