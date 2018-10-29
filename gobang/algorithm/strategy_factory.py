# -*- coding: utf-8 -*-

# @Author   : Shichao Liao
# @Email    : liaosc@liaoshichao.com
# @Site     : https://liaoshichao.com/
# @Github   : https://github.com/liaoscdy

from gobang.algorithm.instance.simple_strategy import SimpleStrategy

class StrategyFactory:

    @staticmethod
    def ProvideInstance():
        return SimpleStrategy()

