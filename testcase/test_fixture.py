import pytest


@pytest.fixture()
def login():
    print("用户登录")
    print("获取token")
    username = "Tom"
    token = "tokenwoerui2323"
    yield [username, token]
    print("结束登录，退出")


def test_case1(login):
    print("测试用例1")
    print(f"用户信息为:{login}")
    pass


def test_case2(connection_db):
    print("测试用例2")
    pass


def test_case3():
    print("测试用例3")
    pass


def test_case4():
    print("测试用例4")
    pass
