import tempfile
import pytest
class C:
    def f(self):
        return 1

    def g(self):
        return 2

@pytest.fixture
def c_instance():
    return C()

@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def setup_teardown():
    print('setup')
    yield
    print('teardown')

def test_with_setup_teardown(setup_teardown):
    print('in test')

def test_f(c_instance, temporary_dir):
    assert c_instance.f() == 1, 'Error. x != 1'
    print(temporary_dir)

def test_g(c_instance):
    assert c_instance.g() == 2, 'Error. x != 2'