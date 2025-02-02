import pytest


@pytest.mark.usefixtures('testdata')
class TestData:
    def test_profileDetails(self,testdata):
        print('Test Data:',testdata)
        for k , v in testdata.items():
            print(v)


