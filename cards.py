def card_value(card, total):
    if card == "A":
        one = total + 1
        eleven = total + 11
        if 21 - eleven < 0:
            return 1
        elif abs(21 - one) < abs(21 - eleven):
            return 1
        else:
            return 11
    elif card == "2":
        return 2
    elif card == "3":
        return 3
    elif card == "4":
        return 4
    elif card == "5":
        return 5
    elif card == "6":
        return 6
    elif card == "7":
        return 7
    elif card == "8":
        return 8
    elif card == "9":
        return 9
    else:
        return 10



