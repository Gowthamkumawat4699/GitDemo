import pytest

from BaseClass import BaseClass


@pytest.mark.usefixtures('dataLoad')
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[1])
        log.info(dataLoad[0])
        print("Test Data:", dataLoad)
