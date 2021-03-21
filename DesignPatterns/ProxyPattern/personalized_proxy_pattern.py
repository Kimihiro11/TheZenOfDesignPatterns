# -*- coding: utf-8 -*-
# @Time : 2021/3/21 17:08 
# @Author : kimihiro
# @File : personalized_proxy_pattern.py 
# @Software: PyCharm
import abc


class AbstractGamePlayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def login(self, user: str, password: str):
        pass

    @abc.abstractmethod
    def kill_boss(self):
        pass

    @abc.abstractmethod
    def upgrade(self):
        pass


class GamePlayer(AbstractGamePlayer):
    def __init__(self, name):
        self._name = name
        self.level = 0

    def login(self, user: str, password: str):
        return "User {0} login as {1} successful.".format(user, self._name)

    def kill_boss(self):
        return "%s is killing boos" % self._name

    def upgrade(self):
        self.level += 1


class AbstractProxy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def count(self):
        pass


class GamePlayerProxy(AbstractGamePlayer, AbstractProxy):
    def __init__(self, gamer: GamePlayer):
        self._gamer = gamer
        self._count = 0

    def login(self, user: str, password: str):
        self._gamer.login(user, password)

    def kill_boss(self):
        self._gamer.kill_boss()

    def upgrade(self):
        self._gamer.upgrade()
        self.count()

    def count(self):
        self._count += 100


class Client:
    def main(self):
        player = GamePlayer("J")
        proxy = GamePlayerProxy(player)
        proxy.login("J.P", "any")
        proxy.kill_boss()
        proxy.upgrade()
        return player, proxy
