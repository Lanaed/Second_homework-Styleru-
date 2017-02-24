def calc_payment(object):
    if object['payment_to'] != 0 and object['payment_from'] != 0:
        payment = (object['payment_to'] + object['payment_from']) / 2
    elif object['payment_to'] == 0 and object['payment_from'] == 0:
        payment = 0
    elif object['payment_from'] == 0:
        payment = object['payment_to']
    elif object['payment_to'] == 0:
        payment = object['payment_from']
    return payment


def calc_vacancies(description, dict, language, payment):
    if description.count(language.lower()) > 0:
        dict[language][0] += 1
        if payment != 0:
            dict[language][1] += payment
            dict[language][2] += 1