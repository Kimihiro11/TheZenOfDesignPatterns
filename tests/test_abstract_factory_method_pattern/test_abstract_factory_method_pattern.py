# -*- coding: utf-8 -*-
# @Time : 2021/2/13 10:51 
# @Author : kimihiro
# @File : test_abstract_factory_method_pattern.py 
# @Software: PyCharm

from DesignPatterns.AbstractFactoryMethodPattern import Client


def test_abstract_factory_method_pattern():
    cli = Client()
    res = cli.main()
    assert res == ["pro A", "pro B"]
