from utils import refactor_input, get_ids, div_by_10
from mock import mock_for_test


usaable_list = {}


def test_refactor_input():

    usaable_list = refactor_input(mock_for_test)
    assert type(usaable_list) is dict


def test_refactor_input_fail():

    usaable_list = refactor_input("str")
    assert "please" in usaable_list


def test_div_by_10():

    d_10 = div_by_10(usaable_list)
    for k, v in d_10.items():
        assert v[0].get("constance_mult")


def test_div_by_10_fail():

    d_10 = div_by_10([])
    assert "please" in d_10


def test_test_get_id():

    ress = get_ids(mock_for_test)
    for res in ress:
        assert type(res) is str


def test_get_id_fail():
    ress = get_ids(mock_for_test)
    for res in ress:
        assert not type(res) is int
