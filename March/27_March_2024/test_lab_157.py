# Fixtures:- pass some of the data to other test cases , ypu can use the fixtures.
# once you defined any fumctions as fixtures, then you just have to pass class name of your fixtures to use it
import pytest
import requests


@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return data


@pytest.fixture
def sample_data2():
    data = [10, 11, 12, 13, 14, 15, ]
    return data






# def test_case_no_1_sample_data_Injected():
#     data2 = sample_data()
#     assert data2 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def test_data_Injected(sample_data):
    assert sample_data == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_data_Injected_multiple(sample_data2):
    assert 13 in sample_data2


