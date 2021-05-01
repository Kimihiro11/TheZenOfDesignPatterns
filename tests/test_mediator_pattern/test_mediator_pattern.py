# -*- coding: utf-8 -*-
# @Time : 2021/5/1 15:30 
# @Author : kimihiro
# @File : test_mediator_pattern.py 
# @Software: PyCharm
from DesignPatterns.MediatorPattern import Consumer, Producer, Mediator


def test_mediator_pattern():
    consumer = Consumer('手机', 3000)
    producer = Producer("手机", 2500)
    mediator = Mediator()
    mediator.consumer = consumer
    mediator.producer = producer
    mediator.complete()
