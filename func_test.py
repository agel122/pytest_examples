import pytest

from func_totest import my_func


def test_correct():
    assert my_func(2) == 3


def test_wrong():
    assert my_func(2) == 4


def test_exception_ok():
    with pytest.raises(ValueError) as error:
        my_func('wrong_data')
    assert "wrong type of data inputted" == error.value.args[0]


def test_exception_nok():
    with pytest.raises(ValueError) as error:
        my_func('wrong_data')
    assert "wrong type of data inputted+1" == error.value.args[0]


@pytest.fixture
def setupdata():
    return 'wrong_data'


def test_exception_ok2(setupdata):
    with pytest.raises(ValueError) as error:
        my_func(setupdata)
    assert "wrong type of data inputted" == error.value.args[0]


if __name__ == '__main__':
    pytest.main()

