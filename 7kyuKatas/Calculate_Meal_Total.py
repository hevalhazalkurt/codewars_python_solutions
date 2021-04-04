
def calculate_total(subtotal, tax, tip):
    return round(sum([subtotal, subtotal*tax/100, subtotal*tip/100]), 2)
