"""
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
"""

# 计算器测试代码
import pytest
import yaml


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


class TestCalc:

    # def setup(self):
    #     print("开始计算")
    #     self.clac = Calculator()
    #
    # def teardown(self):
    #     print("计算结束")

    # @pytest.fixture()
    # def caculate(self):
    #     print("开始计算")
    #
    #     yield
    #     print("计算结束")

    @pytest.mark.parametrize("a,b,expect", adddatas_data,
                             ids=myid_add)
    @pytest.mark.run(order=1)
    def test_add(self, a, b, expect, get_calc, caculate):
        # 实例化计算机类
        # clac = Calculator()
        if isinstance(a, str):
            print("非数字类型")
            assert False

        elif a is None:
            print("不能为空")
            assert False

        elif 999999 <= a or a <= -999999:
            print("超出最大值")
            assert False

        else:
            # 调用conftest里面的方法
            result = get_calc.add(a, b)
            # 浮点数的判断
            if isinstance(result, float):
                result = round(result, 2)
            # 得到结果之后验证
            assert result == expect

    # 除法运算
    @pytest.mark.parametrize("a,b,expect", divdatas_data, ids=myid_div)
    @pytest.mark.run(order=4)
    def test_div(self, a, b, expect, get_calc, caculate):
        # 判断b不能等于0
        if b == 0:
            print("除数不能等于0")
            assert False

        elif a is None:
            print("不能为空")
            assert False

        elif 999999 <= a or a <= -999999:
            print("不能低于最小值")
            assert False

        # 调用conftest里面的方法
        else:
            result = get_calc.div(a, b)
            if isinstance(result, float):
                result = round(result, 2)

            assert result == expect

    # 减法运算
    @pytest.mark.parametrize("a,b,expect", subdatas_data)
    @pytest.mark.run(order=2)
    def test_sub(self, a, b, expect, get_calc):

        if isinstance(a, str):
            print("非数字类型")
            assert False

        elif a is None:
            print("不能为空")
            assert False

        elif 999999 <= b or b <= -999999:
            print("超出最大值")
            assert False

        else:
            # 调用conftest里面的方法
            result = get_calc.sub(a, b)
            # 浮点数的判断
            if isinstance(result, float):
                result = round(result, 2)
            # 得到结果之后验证
            assert result == expect

    # 乘法运算
    @pytest.mark.parametrize("a,b,expect", muldatas_data)
    @pytest.mark.run(order=3)
    def test_mul(self, a, b, expect, get_calc, caculate):
        if isinstance(a, str):
            print("非数字类型")
            assert False

        elif a is None:
            print("不能为空")
            assert False

        elif 999999 <= a or a <= -999999:
            print("超出最大值")
            assert False

        else:
            # 调用conftest里面的方法
            result = get_calc.mul(a, b)
            # 浮点数的判断
            if isinstance(result, float):
                result = round(result, 2)
            # 得到结果之后验证
            assert result == expect
