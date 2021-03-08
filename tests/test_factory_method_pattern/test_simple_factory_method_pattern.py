# -*- coding: utf-8 -*-
# @Time : 2021/2/11 13:42 
# @Author : kimihiro
# @File : test_simple_factory_method_pattern.py 
# @Software: PyCharm

from DesignPatterns.FactoryMethodPattern.simple_factory_method_pattern import Client


def test_simple_factory_method_pattern():
    client = Client()
    color_list, talk_list = client.run()

    assert color_list == ['white', 'black', 'yellow']
    assert talk_list == ['I am white human', 'I am black human', 'I am yellow human']
