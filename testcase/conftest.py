import pytest
import yaml

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


with open('./test_data/calc.yaml') as f:
    datas = yaml.safe_load(f)
    adddatas = datas['add']
    adddatas_data = adddatas['datas']
    myid_add = adddatas['myid']

    divdatas = datas['div']
    divdatas_data = divdatas['datas']
    myid_div = divdatas['myid']

    subdatas = datas["sub"]
    subdatas_data = subdatas['datas']

    muldatas = datas['mul']
    muldatas_data = muldatas['datas']


# 不想用parametrize方法，也想用fixture方法,定义一个方法，获取数据
@pytest.fixture(params=adddatas_data, ids=myid_add)
def get_data_add(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为{data}")

    yield data
    print("结束测试")


@pytest.fixture(params=divdatas_data, ids=myid_div)
def get_data_div(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为{data}")
    yield data
    print("结束测试")


@pytest.fixture()
def caculate():
    print("开始计算")

    yield
    print("计算结束")
