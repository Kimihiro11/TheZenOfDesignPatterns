# -*- coding: utf-8 -*-
# @Time : 2021/3/21 16:11 
# @Author : kimihiro
# @File : common_proxy_pattern.py 
# @Software: PyCharm
from DesignPatterns.ProxyPattern import AbstractGamePlayer


class GamePlayer(AbstractGamePlayer):
    def __init__(self, abs_gamer: AbstractGamePlayer, name: str):
        if abs_gamer is None:
            raise Exception("Can not create real gamer")
        self._name = name
        self.level = 0

    def login(self, user: str, password: str):
        return "User {0} login as {1} successful.".format(user, self._name)

    def kill_boss(self):
        return "%s is killing boos" % self._name

    def upgrade(self):
        self.level += 1


class GamePlayerProxy(AbstractGamePlayer):
    def __init__(self, name: str):
        self._gamer = GamePlayer(self, name)

    def login(self, user: str, password: str):
        self._gamer.login(user, password)

    def kill_boss(self):
        self._gamer.kill_boss()

    def upgrade(self):
        self._gamer.upgrade()


class Client:
    def main(self):
        proxy = GamePlayerProxy("J")
        proxy.login("J.P", "any")
        proxy.kill_boss()
        proxy.upgrade()
        return proxy
