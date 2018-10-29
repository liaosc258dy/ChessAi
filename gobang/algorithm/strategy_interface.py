# -*- coding: utf-8 -*-

# @Author   : Shichao Liao
# @Email    : liaosc@liaoshichao.com
# @Site     : https://liaoshichao.com/
# @Github   : https://github.com/liaoscdy


class StrategyInterface():
    @staticmethod
    def GetChessEffective(chessMat, x, y, chessType):
        if 0 <= x <= 14 \
                and 0 <= y <= 14:
            if chessMat[x][y] == chessType:
                return 1
        return 0
    
    @staticmethod
    def IsGobangWin(chessMat, x, y):
        chessType = chessMat[x][y]
        # 横,竖,撇,捺
        chessDirection = [1 for n in range(4)]
        for i in range(5):
            if chessDirection[0] >= 5 \
                    or chessDirection[1] >= 5 \
                    or chessDirection[2] >= 5 \
                    or chessDirection[3] >= 5:
                return True
            xLeftPos = x - i - 1
            xRightPos = x + i + 1
            yUpPos = y - i - 1
            yDownPos = y + i + 1

            chessDirection[0] = chessDirection[0] + StrategyInterface.GetChessEffective(chessMat, xRightPos, y, chessType)
            chessDirection[0] = chessDirection[0] + StrategyInterface.GetChessEffective(chessMat, xLeftPos, y, chessType)
            chessDirection[1] = chessDirection[1] + StrategyInterface.GetChessEffective(chessMat, x, yUpPos, chessType)
            chessDirection[1] = chessDirection[1] + StrategyInterface.GetChessEffective(chessMat, x, yDownPos, chessType)
            chessDirection[2] = chessDirection[2] + StrategyInterface.GetChessEffective(chessMat, xRightPos, yUpPos, chessType)
            chessDirection[2] = chessDirection[2] + StrategyInterface.GetChessEffective(chessMat, xLeftPos, yDownPos, chessType)
            chessDirection[3] = chessDirection[3] + StrategyInterface.GetChessEffective(chessMat, xLeftPos, yUpPos, chessType)
            chessDirection[3] = chessDirection[3] + StrategyInterface.GetChessEffective(chessMat, xRightPos, yDownPos, chessType)
        return False

    def DecideNext(self, chessMat, chessType, callBack):
        """  Decide next
        return pointX, pointY
        """
        pass

