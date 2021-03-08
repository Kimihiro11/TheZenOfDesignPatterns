# -*- coding: utf-8 -*-
# @Time : 2021/2/11 13:49 
# @Author : kimihiro
# @File : muliti_factory_method_pattern.py 
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


class AbsHumanFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_human(self) -> AbsHuman:
        pass


class WhiteFactory(AbsHumanFactory):
    def create_human(self) -> WhiteHuman:
        return WhiteHuman()


class BlackFactory(AbsHumanFactory):
    def create_human(self) -> BlackHuman:
        return BlackHuman()


class YellowFactory(AbsHumanFactory):
    def create_human(self) -> YellowHuman:
        return YellowHuman()


class Client:
    @classmethod
    def run(cls):
        w_h = WhiteFactory().create_human()
        b_h = BlackFactory().create_human()
        y_h = YellowFactory().create_human()
        color_list = [w_h.get_color(), b_h.get_color(), y_h.get_color()]
        human_talk = [w_h.talk(), b_h.talk(), y_h.talk()]
        return color_list, human_talk
