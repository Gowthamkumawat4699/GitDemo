import pytest

@pytest.mark.xfail
def test_secondprogram() :
    text = 'hello'
    print(text)
    assert text == 'hi' , "actual text not matched with the expected text"


@pytest.mark.regression
def test_creditcard() :
    print("I have credit card in the ICICI bank")


