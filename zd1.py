def card_hide(card):
    return "*" * len(card[:-4]) + card[-4:]
print(card_hide(input('Введите номер карты:')))