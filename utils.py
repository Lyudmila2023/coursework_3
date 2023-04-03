import json
from datetime import datetime


def load_data():
    """Выгружаем данные из json"""
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def sort_data(data, filtered_empty_from):
    data = [i for i in data if 'state' in i and i['state'] == 'EXECUTED']
    if filtered_empty_from:
        data = [i for i in data if 'from' in i]
    return data


def sort_operations(data, count_operations):
    data = sorted(data, key=lambda i: i['date'], reverse=True)
    return data[:count_operations]


def final_form(data):
    list_operations = []
    for i in data:
        date = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = i['description']
        if 'from' in i:
            sender = i['from'].split()
            sender_bill = sender.pop(-1)
            sender_bill = f'{sender_bill[:4]}{sender_bill[4:6]}** ****{sender_bill[-4:]}'
            bill_type = ' '.join(sender)
        else:
            sender_bill, bill_type = "Cчет скрыт", ""
        recipient = i["to"].split()
        recipient_bill = recipient.pop(-1)
        recipient_bill = f'**{recipient_bill[-4:]}'
        to_info = ' '.join(recipient)
        amount = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
        list_operations.append(f"""
{date} {description}
{bill_type} {sender_bill} -> {to_info} {recipient_bill}
{amount}
""")
    return list_operations
