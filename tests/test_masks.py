from src.masks import mask_account_number, mask_card_number
import pytest
from tests.fixtures import (
    data_for_masks_number,
    result_for_masks_number,
)


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("5500320044006600", "5500 32** **** 6600"),
        ("4455000033226699", "4455 00** **** 6699"),
    ],
)
def test_mask_card_number(input_data, expected_output):
    assert mask_card_number(input_data) == expected_output


def test_mask_account_number(data_for_masks_number, result_for_masks_number):
    assert mask_account_number(data_for_masks_number) == result_for_masks_number
