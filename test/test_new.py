from main import func
import pytest

@pytest.fixture
def fixture_one(scope='session'):
    print("\nHey, this is fixture one!")
    yield
    print("\nBye from fixture one!")
@pytest.fixture
def fixture_two(fixture_one):
    print("\nHey, this is fixture two!")
    yield
    print("\nBye from fixture two!")





def test_func_good1():
        assert func(5, 6)==11


@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 15),
                                                   (1, 5, 6),
                                                   (-5, -3, -8),
                                                   (125, -115, 10)])
def test_func_good2(a, b, expected_result):
      assert func(a, b)==expected_result

@pytest.mark.parametrize(" a,  expected_result", [('table', 5),
                                                 ('fox', 3)])
def test_func_lenght(a, expected_result):
    assert len(a) == expected_result

def test_function(fixture_two):
    print("\nHey, I'm test function!")
# @pytest.fixture
# def fixture_one():
#     print("\nHey, this is fixture one!")
#     yield
#     print("\nBye from fixture one!")
#
#
# @pytest.fixture
# def fixture_two(fixture_one):
#     print("\nHey, this is fixture two!")
#     yield
#     print("\nBye from fixture two!")
#
#
# def test_function(fixture_two):
#     print("\nHey, I'm test function!")