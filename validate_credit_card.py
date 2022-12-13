import re

def valid(card: str):
    result = re.findall(r'^[456]\d{3}-\d{4}-\d{4}-\d{4}$|^[456]\d{3}\d{4}\d{4}\d{4}$', card)
    if result:
        result = ''.join(re.split(r'-', result[0]))
        if re.findall(r'1{4,}|2{4,}|3{4,}|4{4,}|5{4,}|6{4,}|7{4,}|8{4,}|9{4,}', result):
            return 'Invalid'
        return 'Valid'
    return 'Invalid'


credit_cards = []
n = int(input())
for _ in range(n):
    credit_cards.append(input())

[print(valid(card)) for card in credit_cards]