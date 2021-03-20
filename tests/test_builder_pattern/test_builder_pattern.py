# -*- coding: utf-8 -*-
# @Time : 2021/3/20 15:35 
# @Author : kimihiro
# @File : test_builder_pattern.py 
# @Software: PyCharm
from DesignPatterns.BuilderPattern import Director


def test_builder_pattern():
    director = Director()
    pro_a = director.get_product_a()

    assert pro_a.do_something() == "pro_a"
