# -*- coding: utf-8 -*-
# @Time : 2021/3/21 15:53 
# @Author : kimihiro
# @File : test_proxy_pattern.py 
# @Software: PyCharm
from DesignPatterns.ProxyPattern import Client
from DesignPatterns.ProxyPattern.common_proxy_pattern import Client as CommonClient
from DesignPatterns.ProxyPattern.force_proxy_pattern import Client as ForceClient
from DesignPatterns.ProxyPattern.personalized_proxy_pattern import Client as PerClient
from DesignPatterns.ProxyPattern.dynamic_proxy_pattern import Client as DyClient


def test_proxy_pattern():
    client = Client()
    p = client.main()
    assert p.level == 1


def test_common_proxy_pattern():
    common = CommonClient()
    proxy_player = common.main()
    assert proxy_player._gamer.level == 1


def test_force_proxy_pattern():
    force = ForceClient()
    real = force.run_real_player_direct()
    proxy = force.run_with_proxy_direct()
    force_proxy = force.run_force_proxy()

    assert real.level == 0
    assert proxy.level == 0
    assert force_proxy.level == 1


def test_personalized_proxy():
    per_client = PerClient()
    gamer, proxy = per_client.main()
    assert gamer.level == 1
    assert proxy._count == 100


def test_dynamic_proxy():
    dy_client = DyClient()
    dy_client = dy_client.main()
    assert dy_client.level == 1
