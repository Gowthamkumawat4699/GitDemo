import pytest
#Any pytest file should start with test_ or end with_test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name should have sense
#-k stands for method names execution, -s logs in out put -v stands for more info metadata
#you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases conftest file to generalize
#fixture and make it available to all test cases(fixture name into parameters of method)
#datadriven and parameterization can be done with return statement in tuple format
#when you define fixture scope to class only,  it will run once before class is initiated  and at the end
# py.test --html=report.html -s  = to create html report

# logs == Debug,info,warning,error and critical


def test_firstprogram():
    print('I am learning pytest concept')

@pytest.mark.skip
def test_firstprogram():
    print('This is my second method which has same name')


def test_greet():
    print("hello world")


def test_add():
    a = 2
    b = 6
    assert a+6 == 8, "addition does not match with expected condition"

@pytest.mark.regression
def test_creditcard():
    print("I have credit card in the HDFC bank")
    print("Get the free credit card from this link if you don't have")

#command + output - run all test file
#py.test -v -s
# test_demo1.py::test_firstprogram This is my second method which has same name
# PASSED
# test_demo1.py::test_greet hello world
# PASSED
# test_demo1.py::test_add PASSED
# test_demo1.py::test_creditcard I have credit card from HDFC bank
# PASSED
# test_demo2.py::test_secondprogram FAILED
# test_demo2.py::test_creditcard I have credit card from ICICI bank
# PASSED
#
# ======================================================================== FAILURES =========================================================================
# ___________________________________________________________________ test_secondprogram ____________________________________________________________________
#
#     def test_secondprogram() :
#         text = 'hello'
# >       assert text == 'hi' , "actual text not matched with the expected text"
# E       AssertionError: actual text not matched with the expected text
# E       assert 'hello' == 'hi'
# E
# E         - hi
# E         + hello
#
# test_demo2.py:3: AssertionError
# ================================================================= short test summary info =================================================================
# FAILED test_demo2.py::test_secondprogram - AssertionError: actual text not matched with the expected text
# =============================================================== 1 failed, 5 passed in 0.08s


# 2.command + output  -- run only methodname with have creditcard
#py.test -m creditcard -v -s
# test_demo1.py::test_creditcard I have credit card from HDFC bank
# PASSED
# test_demo2.py::test_creditcard I have credit card from ICICI bank
# PASSED
#
# ============================================================= 2 passed, 4 deselected in 0.02s


# 3. command + output --- run with has mark as regression
# py.test -m regression -v -s
# test_demo1.py::test_creditcard I have credit card in the HDFC bank
# PASSED
# test_demo2.py::test_creditcard I have credit card in the ICICI bank
# PASSED
#
# ==================================================================== warnings summary =====================================================================
# test_demo1.py:21
#   C:\Users\91709\PycharmProjects\PythonProject\pytestsdemo\test_demo1.py:21: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.regression
#
# test_demo2.py:9
#   C:\Users\91709\PycharmProjects\PythonProject\pytestsdemo\test_demo2.py:9: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.regression
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ======================================================= 2 passed, 4 deselected, 2 warnings in 0.03s

# 4. command + output -- run - skip the test method
# py.test -v -s
# collected 6 items
#
# test_demo1.py::test_firstprogram SKIPPED (unconditional skip)
# test_demo1.py::test_greet hello world
# PASSED
# test_demo1.py::test_add PASSED
# test_demo1.py::test_creditcard I have credit card in the HDFC bank
# PASSED
# test_demo2.py::test_secondprogram FAILED
# test_demo2.py::test_creditcard I have credit card in the ICICI bank
# PASSED


# 4. command + output --- xfail mark
# py.test -v -s
# test_demo1.py::test_firstprogram SKIPPED (unconditional skip)
# test_demo1.py::test_greet hello world
# PASSED
# test_demo1.py::test_add PASSED
# test_demo1.py::test_creditcard I have credit card in the HDFC bank
# PASSED
# test_demo2.py::test_secondprogram XFAIL
# test_demo2.py::test_creditcard I have credit card in the ICICI bank
# PASSED
#
# ==================================================================== warnings summary =====================================================================
# test_demo1.py:23
#   C:\Users\91709\PycharmProjects\PythonProject\pytestsdemo\test_demo1.py:23: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.regression
#
# test_demo2.py:10
#   C:\Users\91709\PycharmProjects\PythonProject\pytestsdemo\test_demo2.py:10: PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.regression
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# =================================================== 4 passed, 1 skipped, 1 xfailed, 2 warnings


