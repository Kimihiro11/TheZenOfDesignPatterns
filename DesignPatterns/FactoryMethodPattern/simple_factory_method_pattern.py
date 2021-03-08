# -*- coding: utf-8 -*-
# @Time : 2021/2/11 13:01 
# @Author : kimihiro
# @File : simple_factory_method_pattern.py 
# @Software: PyCharm
import abc
from typing import Union


class AbsHuman(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_color(self):
        pass

    @abc.abstractmethod
    def talk(self):
        pass


class WhiteHuman(AbsHuman):
    def get_color(self):
        return "white"

    def talk(self):
        return "I am white human"


class BlackHuman(AbsHuman):
    def get_color(self):
        return "black"

    def talk(self):
        return "I am black human"


class YellowHuman(AbsHuman):
    def get_color(self):
        return "yellow"

    def talk(self):
        return "I am yellow human"


class HumanFactory:
    @classmethod
    def create_human(cls, human_cls) -> Union[WhiteHuman, BlackHuman, YellowHuman]:
        human = human_cls()
        return human


class Client:
    @classmethod
    def run(cls):
        human_factory = HumanFactory()
        w_h = human_factory.create_human(WhiteHuman)
        b_h = human_factory.create_human(BlackHuman)
        y_h = human_factory.create_human(YellowHuman)
        color_list = [w_h.get_color(), b_h.get_color(), y_h.get_color()]
        human_talk = [w_h.talk(), b_h.talk(), y_h.talk()]
        return color_list, human_talk

