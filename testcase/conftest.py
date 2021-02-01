import pytest

from test_code.calc import Calculator


@pytest.fixture(scope='session')
def connection_db():
    print("连接数据库")
    yield
    print("断开数据库")


@pytest.fixture(scope='module')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

@pytest.fixture()
def caculate():
    print("开始计算")

    yield
    print("计算结束")