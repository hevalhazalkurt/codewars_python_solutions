
def delete_nth(order,max_e):
    new_order = []

    for n in order:
        if new_order.count(n) >= max_e:
            continue
        else:
            new_order.append(n)
    return new_order
