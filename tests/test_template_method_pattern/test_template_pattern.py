# -*- coding: utf-8 -*-
# @Time : 2021/3/20 13:39 
# @Author : kimihiro
# @File : test_template_pattern.py 
# @Software: PyCharm

from DesignPatterns.TemplateMethodPattern import Client


def test_template_pattern():
    client = Client()
    res1, res2 = client.run()
    assert res1.a == 1
    assert res2.a == 3
    assert res1.b == 2
    assert res2.b == 4

    res1.i_am_five()
    res2.i_am_five()
    assert res1.a == 5
    assert res2.a == 5
