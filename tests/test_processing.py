from src.processing import sort_date, state_into
from tests.fixtures import data_sort_date, data_state_into


def test_state_into(data_state_into):
    assert (state_into(data_state_into[0])) == data_state_into[1]


def test_sort_date(data_sort_date):
    assert sort_date(data_sort_date[0]) == data_sort_date[1]
