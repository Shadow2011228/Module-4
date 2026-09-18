from дз import *

def test_check_login():
    assert check_login(name= "!кеша")
    assert check_login(phone = 780904237)
    # assert check_login(phone=)
test_check_login()
