def detect_interaction(customer, seller):

    distance = abs(customer.x - seller.x)

    if distance < 80:
        return True

    return False