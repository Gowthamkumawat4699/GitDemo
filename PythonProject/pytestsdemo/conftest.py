import pytest

@pytest.fixture(scope='class')
def setup():
    print('I am going to print at first')
    yield
    print('I am going to print at last')



# data driven fixture
@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Gowtham","Kumawat","k@4699@gmail.com"]



# data driven fixture it return the data to the test_profiledetail.py
@pytest.fixture()
def testdata():
    print("user profile details")
    return {'first name':'Gowtham','last name':'M','age': '26'}



#parameterization using fixtures
@pytest.fixture(params=[('chrome','Gowtham'),('firebox','kumawat'),'edge'])
def crossBrowser(request):
    print("Test with different browser")
    return request.param