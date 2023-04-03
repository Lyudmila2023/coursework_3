from utils import load_data, sort_data, sort_operations, final_form
import pytest

def test_load_data():
    data = load_data()
    print(data)


def test_sort_data(test_data):
    assert len(sort_data(test_data, filtered_empty_from=True)) == 2


def test_sort_operations(test_data):
    data = sort_operations(test_data, 2)
    assert [i['date'] for i in data] == ['2019-11-19T09:22:25.899614', '2019-02-14T03:09:23.006652']


def test_final_form(test_data):
    data = final_form(test_data[:1])
    assert data[0] == "\n19.11.2019 Перевод организации\nMaestro 781084** ****5568 -> Счет **2869\n30153.72 руб.\n"
