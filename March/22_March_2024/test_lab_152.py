import pytest


# python -m pytest --html=report.html --->used to generate html reports
# pytest -m smoke Mar/22_March_2024/test_lab152.py` ----> marking the test cases as used.

# ALLURE REPORT PROCCESS
#install- pip install allure-pytest
#npm i -g allure-commandline

# Allure repots command:-  python -m pytest .\March\22_March_2024\test_lab_152.py  --alluredir="C:\Users\new ssd\PycharmProjects\PyLearning2x\allure-results"

#run next command:- allure serve allure-results




def test_sub1():
    assert 2 + 2 == 4


@pytest.mark.smoke
def test_sub2():
    assert 2 - 2 == 0


@pytest.mark.reg
def test_add2():
    assert 2 + 2 == 4


@pytest.mark.skip(reason="Not implemented yet")
def test_multi():
    assert 2 * 2 ==4
