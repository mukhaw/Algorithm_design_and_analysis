from filecmp import cmp
import os
import pytest
from homeworks.binary_search_trees import find_number_in_tree
def test_load_binary_search_returns_list_of_found_elements():
    find_number_in_tree(os.path.dirname(__file__) + "/1.in")
    expected_result = cmp('/home/mukha/PycharmProjects/Algorithm_design_and_analysis/homeworks/bintrees.out',os.path.dirname(__file__) + "/1.contains.out")
    assert expected_result is True
def test_2():
    find_number_in_tree(os.path.dirname(__file__) + "/2.in")
    expected_result = cmp('/home/mukha/PycharmProjects/Algorithm_design_and_analysis/homeworks/bintrees.out',
                          os.path.dirname(__file__) + "/2.contains.out")
    assert expected_result is True
