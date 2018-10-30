# -*- coding: utf-8 -*-

# @Author   : Shichao Liao
# @Email    : liaosc@liaoshichao.com
# @Site     : https://liaoshichao.com/
# @Github   : https://github.com/liaoscdy

from gobang.algorithm.strategy_interface import StrategyInterface
from gobang.ui.chess_item import ChessType

class SimpleStrategy(StrategyInterface):

    def DecideNext(self, chessMat, chessType, callBack):
        for y in range(14):
            for x in range(14):
                if chessMat[x][y] == ChessType.NOP.value:
                    callBack(x, y)
                    return
        callBack(0, 0)
