# -*- coding: utf-8 -*-
# @Time : 2021/3/21 16:29 
# @Author : kimihiro
# @File : force_proxy_pattern.py 
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

    @abc.abstractmethod
    def get_proxy(self):
        pass


class GamePlayer(AbstractGamePlayer):
    def __init__(self, name: str):
        self._name = name
        self.level = 0
        self._proxy = None

    def get_proxy(self):
        self._proxy = GamePlayerProxy(self)
        return self._proxy

    def login(self, user: str, password: str):
        if self._is_proxy:
            return "User {0} login as {1} successful.".format(user, self._name)
        else:
            return 0

    def kill_boss(self):
        if self._is_proxy():
            return "%s is killing boos" % self._name
        else:
            return 0

    def upgrade(self):
        if self._is_proxy():
            self.level += 1

    def _is_proxy(self):
        if self._proxy is None:
            return False
        return True


class GamePlayerProxy(AbstractGamePlayer):
    def __init__(self, gamer: GamePlayer):
        self._gamer = gamer

    def login(self, user: str, password: str):
        self._gamer.login(user, password)

    def kill_boss(self):
        self._gamer.kill_boss()

    def upgrade(self):
        self._gamer.upgrade()

    def get_proxy(self):
        return self


class Client:
    def run_real_player_direct(self):
        player = GamePlayer("J")
        player.login("J.P", "any")
        player.kill_boss()
        player.upgrade()
        return player

    def run_with_proxy_direct(self):
        player = GamePlayer("J")
        proxy = GamePlayerProxy(player)
        proxy.login("J.P", "any")
        proxy.kill_boss()
        proxy.upgrade()
        return player

    def run_force_proxy(self):
        player = GamePlayer("J")
        proxy = player.get_proxy()
        proxy.login("J.P", "any")
        proxy.kill_boss()
        proxy.upgrade()
        return player
