from src.widget import change_date, check_bill
from tests.fixtures import data_change_date, data_check_bill


def test_check_bill(data_check_bill):
    assert check_bill(data_check_bill[0]) == data_check_bill[1]
    assert check_bill(data_check_bill[2]) == data_check_bill[3]


def test_change_date(data_change_date):
    assert change_date(data_change_date[0]) == data_change_date[1]
