
def get_order(order):
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    return "".join([(i + " ") * order.count(i.lower()) for i in menu if i.lower() in order]).rstrip()
