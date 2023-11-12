from pytest import fixture


@fixture()
def data_for_masks_number():
    return "73654108430135874305"


@fixture()
def result_for_masks_number():
    return "**4305"


@fixture()
def data_check_bill():
    return (
        "Счет 64686473678894779589",
        "Счет **9589",
        "Maestro 1596837868705199",
        "Maestro 1596 83** **** 5199",
    )


@fixture()
def data_change_date():
    return "2018-07-11T02:26:18.671407", "11.07.2018"


@fixture()
def data_state_into():
    return [{"state": "CANCELED"}, {"state": "EXECUTED"}], [{"state": "EXECUTED"}]


@fixture()
def data_sort_date():
    return (
        [{"date": "2021-01-01"}, {"date": "2020-01-01"}, {"date": "2019-01-01"}],
        [{"date": "2019-01-01"}, {"date": "2020-01-01"}, {"date": "2021-01-01"}],
    )
