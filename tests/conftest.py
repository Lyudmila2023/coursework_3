import pytest


@pytest.fixture
def test_data():
    return [{
        "id": 154927927,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {
            "amount": "30153.72",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 7810846596785568",
        "to": "Счет 43241152692663622869"
    },
        {
            "id": 743628025,
            "state": "EXECUTED",
            "date": "2018-06-04T06:59:55.424356",
            "operationAmount": {
                "amount": "978.31",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 61834060137088759145"
        },
        {
            "id": 743278119,
            "state": "EXECUTED",
            "date": "2018-10-15T08:05:34.061711",
            "operationAmount": {
                "amount": "51203.12",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1435442169918409",
            "to": "Maestro 7452400219469235"
        },
        {
            "id": 871921546,
            "state": "CANCELED",
            "date": "2019-02-14T03:09:23.006652",
            "operationAmount": {
                "amount": "47022.09",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 6216537926639975",
            "to": "Счет 67667879435628279708"
        },
        {
            "id": 373912477,
            "date": "2018-03-09T02:11:01.339352",
            "operationAmount": {
                "amount": "33249.01",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 7022985698476865",
            "to": "Счет 60979028617970883410"
        }]