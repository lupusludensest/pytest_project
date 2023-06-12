import tempfile
import pytest
class C:
    def f(self):
        return 1

    def g(self):
        return 2

@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def c_instance(temporary_dir):
    return C()
@pytest.fixture(autouse=True, scope='session')
def setup_teardown():
    print('setup')
    yield
    print('teardown')

@pytest.fixture(name='fix')
def ugly_name_function_to_use_in_test(): # pytest -s pytest_fixture_2.py -k ugly_name_function_to_use_in_test
    return f'ugly_name_function_to_use_in_test renamed'

@pytest.fixture(params=(1, 2, 3, 4))
def an_int(request):
    yield request.param + 2

def test_an_int(an_int): # pytest -s pytest_fixture_2.py -k test_an_int
    print(f'got {an_int=}')


def test_with_setup_teardown(fix): # pytest -s pytest_fixture_2.py -k test_with_setup_teardown
    print(f'in test, used {fix=}')

def test_f(c_instance, temporary_dir):
    assert c_instance.f() == 1, 'Error. x != 1'
    print(temporary_dir)

@pytest.mark.usefixtures('setup_teardown') # pytest -s pytest_fixture_2.py -k test_g
def test_g(c_instance):
    assert c_instance.g() == 2, 'Error. x != 2'

class TestMyThing: # pytest -s pytest_fixture_2.py -k TestMyThing
    @pytest.fixture
    def fix(self):
        yield 10

    def test_1(self, fix):
        print(f'got = {fix=}')
