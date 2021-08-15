from main import func_1
import pytest
import random



# def test_function(method_two):
#     print("\nTEST -1 ")

 # c= 'study'
 # d='work'

def test_age(method_three):
    print(f'method three return - {method_three}')
    assert method_three == 59

#
# @pytest.mark.parametrize("c, d, expected_result", [(24, 36, test_age),
#                                                    (18, 42, test_age),
#                                                    (20, 40, method_three),
#                                                    (18, 40, method_three)])
# def test_func_good2(c, d, expected_result):
#     assert func_1(c, d) == expected_result