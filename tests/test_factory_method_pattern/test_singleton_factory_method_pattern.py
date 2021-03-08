# -*- coding: utf-8 -*-
# @Time : 2021/2/11 14:26 
# @Author : kimihiro
# @File : test_singleton_factory_method_pattern.py 
# @Software: PyCharm
from DesignPatterns.FactoryMethodPattern.singleton_factory_method_pattern import Client


def test_singleton_factory_method_pattern():
    def set_name(self, name: str):
        setattr(self, "_name", name)

    def get_name(self):
        return self._name

    func_dict = {
        "set_name": set_name,
        "get_name": get_name
    }
    client = Client()
    new_cls = client.get_singleton_cls("Single", func_dict)
    new_cls_obj = new_cls()
    new_cls_obj.set_name("Zoo")
    assert new_cls_obj.get_name() == "Zoo"
