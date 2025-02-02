import pytest


@pytest.mark.usefixtures('setup')
class TestExample:

    def test_fixturedemo2(self):
         print('I am going print in the middle2')

    def test_fixturedemo3(self):
         print('I am going print in the middle3')

    def test_fixturedemo4(self) :
        print('I am going print in the middle4')

    def test_fixturedemo5(self) :
        print('I am going print in the middle5')


#command
#py.test test_fixtureDemo2.py -v -s
# output
# collected 4 items
#
# test_fixtureDemo2.py::TestExample::test_fixturedemo2 I am going to print at first
# I am going print in the middle2
# PASSEDI am going to print at last
#
# test_fixtureDemo2.py::TestExample::test_fixturedemo3 I am going to print at first
# I am going print in the middle3
# PASSEDI am going to print at last
#
# test_fixtureDemo2.py::TestExample::test_fixturedemo4 I am going to print at first
# I am going print in the middle4
# PASSEDI am going to print at last
#
# test_fixtureDemo2.py::TestExample::test_fixturedemo5 I am going to print at first
# I am going print in the middle5
# PASSEDI am going to print at last


# command + output ---- scope='class' in the conftest.py so the after test will be run only once after all the method execution complete for the class
#py.test test_fixtureDemo2.py -v -s
#collected 4 items

# test_fixtureDemo2.py::TestExample::test_fixturedemo2 I am going to print at first
# I am going print in the middle2
# PASSED
# test_fixtureDemo2.py::TestExample::test_fixturedemo3 I am going print in the middle3
# PASSED
# test_fixtureDemo2.py::TestExample::test_fixturedemo4 I am going print in the middle4
# PASSED
# test_fixtureDemo2.py::TestExample::test_fixturedemo5 I am going print in the middle5
# PASSEDI am going to print at last