import os
from typing import List

import pytest
from homeworks.binary_search_by_answer import get_length_of_section
def get_data_for_testing(file_name:str)->List[int]:
    with open(file_name) as f:
        file = f.readline()
    return int(file.rstrip('\n'))

@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/1_bs_by_ans.in", get_data_for_testing(os.path.dirname(__file__) + "/1_bs_by_ans.out")),
        (os.path.dirname(__file__) + "/2_bs_by_ans.in", get_data_for_testing(os.path.dirname(__file__) + "/2_bs_by_ans.out")),
        (os.path.dirname(__file__) + "/3_bs_by_ans.in", get_data_for_testing(os.path.dirname(__file__) + "/3_bs_by_ans.out")),
        (os.path.dirname(__file__) + "/4_bs_by_ans.in", get_data_for_testing(os.path.dirname(__file__) + "/4_bs_by_ans.out")),
        (os.path.dirname(__file__) + "/5_bs_by_ans.in", get_data_for_testing(os.path.dirname(__file__) + "/5_bs_by_ans.out")),
    ],
)
def test_load_binary_search_returns_list_of_found_elements(file_name: str, expected_result: int):
    actual_result = get_length_of_section(file_name)
    assert actual_result == expected_result