import os
from typing import Tuple,List

import pytest
from homeworks.hw_01 import load_binary_search_with_data,get_data,binary_search
def get_data_for_testing(file_name:str)->List[int]:
    with open(file_name) as f:
        file = f.readlines()
    return [int(i.rstrip('\n')) for i in file]

@pytest.mark.parametrize(
    ("file_name", "expected_result"),
    [
        (os.path.dirname(__file__) + "/1.in", get_data_for_testing(os.path.dirname(__file__) + "/1.out")),
        (os.path.dirname(__file__) + "/2.in", get_data_for_testing(os.path.dirname(__file__) + "/2.out")),
        (os.path.dirname(__file__) + "/3.in", get_data_for_testing(os.path.dirname(__file__) + "/3.out")),
        (os.path.dirname(__file__) + "/4.in", get_data_for_testing(os.path.dirname(__file__) + "/4.out")),
        (os.path.dirname(__file__) + "/5.in", get_data_for_testing(os.path.dirname(__file__) + "/5.out")),
    ],
)
def test_load_binary_search_returns_list_of_found_elements(file_name: str, expected_result: Tuple[int, int]):
    actual_result = load_binary_search_with_data(file_name)
    assert actual_result == expected_result