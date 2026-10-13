def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        return 40
    elif item == "biriyano":
        return 70
    else:
        return 0


def item_cost(item, qty):
    amount=get_price(item)*qty
    return amount

    
    # TODO: call get_price() and return the cost


def calculate_gst(amount, rate=0.05): 
    gst= amount*rate
    return gst
    # TODO: return the GST rounded to 2 decimals


def generate_bill(subtotal, discount_percent=0):
    discount=subtotal*discount_percent
    amount_after_discount=subtotal-discount
    gst = calculate_gst(subtotal,rate=0.05)
    total =amount_after_discount+gst
    return discount,gst,total


def split_bill(total, people):
    each_pays =total/people # TODO
    left_over = # TODO
    return # TODO


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

subtotal = # TODO: call item_cost() for dosa and coffee and add them
discount, gst, total = # TODO: call generate_bill() using a KEYWORD argument
each, extra = # TODO: call split_bill() with the total (as a whole number) and 3 people

print("Subtotal :", subtotal)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total)
print("Each pays:", each, "| Left over:", extra)